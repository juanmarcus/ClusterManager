'''
Created on Sep 16, 2009

@author: Juan Ibiapina
'''
from threading import Thread
import Queue
import logging

class Worker(Thread):
    def __init__(self, number, node, queue, controller):
        Thread.__init__(self)
        self.logger = logging.getLogger("Worker:%s:%d" % (node.getInfo().getName(), number))
        self.logger.debug("initializing")
        self.node = node
        self.number = number
        self.remoteworker = node.createRemoteWorker()
        self.queue = queue
        self.controller = controller
        self.filemanager = self.controller.getFileManager()
        
    def run(self):
        self.remoteworker.init(self.node.info)
        while not self.queue.empty():
            # Get a job
            try:
                job = self.queue.get(True, 2)
            except Queue.Empty:
                continue
            jobname = job.getName()
            self.logger.info("got job: %s" % jobname)
            self.logger.info("checking input files")
            
            # Send files
            files = job.getFiles()
            for file in files.values():
                if file.hasAutoSend():
                    self.filemanager.sendFile(self.node, file)
                    
            # Run job and get results
            self.logger.info("running job")
            results = self.remoteworker.runJob(job)
            job.setResults(results)
            
            #check job results
            if not results.getJobResult():
                self.logger.error(results.getJobError())
            else:
                self.logger.info("job finished fine")
                #check task results
                taskresults = results.getTaskResults()
                for tn, tresult in zip(xrange(128), taskresults):
                    self.logger.info("task %d: return code: %d; output:\n%s" % (tn, tresult[0], tresult[1]))
            
            #receiving and deleting files
            self.logger.info("checking output files")
            for file in files.values():
                if file.hasAutoFetch():
                    self.filemanager.fetchFile(self.node, file)
                if file.hasAutoRemove():
                    self.filemanager.removeFile(self.node, file)
            self.logger.info("file transfers completed")
            self.queue.task_done()
        self.logger.info("done")
