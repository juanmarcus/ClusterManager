'''
Created on Sep 16, 2009

@author: Juan Ibiapina
'''
from threading import Thread
import Queue
import logging

class Worker(Thread):
    def __init__(self, client, queue):
        Thread.__init__(self)
        self.logger = logging.getLogger("Worker:%s" % client.getInfo().getName())
        self.logger.debug("initializing")
        self.client = client
        self.clientapi = self.client.getClientAPI()
        self.queue = queue
        
    def run(self):
        self.clientapi.setClientInfo(self.client.info)
        while not self.queue.empty():
            #get job
            try:
                job = self.queue.get(True, 2)
            except Queue.Empty:
                continue
            jobname = job.getName()
            self.logger.info("got job: %s" % jobname)
            self.logger.info("checking input files")
            
            #check files and send to client
            files = job.getFiles()
            for name, file in files.items():
                if file.hasAutoSend():
                    self.logger.info("sending file: %s" % name)
                    self.client.sendFile(file)
                    
            #send job to client
            self.logger.info("running job")
            results = self.clientapi.runJob(job)
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
                    pass
            
            self.logger.info("checking output files")
            #receiving and deleting files
            for name, file in files.items():
                if file.hasAutoFetch():
                    self.logger.info("fetching file: %s" % name)
                    self.client.fetchFile(file)
                if file.hasAutoRemove():
                    self.logger.info("removing file: %s" % name)
                    self.client.removeFile(file)
            self.queue.task_done()
