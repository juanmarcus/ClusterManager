'''
Created on Sep 16, 2009

@author: Juan Ibiapina
'''
from threading import Thread
import Queue
import logging

class Worker(Thread):
    def __init__(self, node, queue, controller):
        Thread.__init__(self)
        self.logger = logging.getLogger("Worker:%s" % node.getInfo().getName())
        self.logger.debug("initializing")
        self.node = node
        self.remoteworker = node.createRemoteWorker()
        self.queue = queue
        self.controller = controller
        self.filemanager = self.controller.getFileManager()
        
    def run(self):
        self.remoteworker.setNodeInfo(self.node.info)
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
            
            self.logger.info("checking output files")
            #receiving and deleting files
            for name, file in files.items():
                if file.hasAutoFetch():
                    self.logger.info("fetching file: %s" % name)
                    self.node.fetchFile(file)
                if file.hasAutoRemove():
                    self.logger.info("removing file: %s" % name)
                    self.node.removeFile(file)
            self.queue.task_done()
