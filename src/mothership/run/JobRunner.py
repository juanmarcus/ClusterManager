'''
Created on Sep 16, 2009

@author: Juan Ibiapina
'''
from threading import Thread
import logging

class JobRunner(Thread):
    def __init__(self, client, queue):
        Thread.__init__(self)
        self.logger = logging.getLogger("JobRunner:%s" % client.getInfo().getName())
        self.logger.info("initializing")
        self.client = client
        self.clientapi = self.client.getClientAPI()
        self.queue = queue
        
    def run(self):
        self.clientapi.setClientInfo(self.client.info)
        while not self.queue.empty():
            #get job
            job = self.queue.get()
            self.logger.info("got job. checking files")
            #check files and send to client
            files = job.getFiles()
            for name, file in files.items():
                if file.exists():
                    self.logger.info("sending file %s" % name)
                    self.client.sendFile(file)
            #send job to client
            self.logger.info("running job")
            result = self.clientapi.runJob(job)
            if not result:
                self.logger.error("problem on job execution")
            self.logger.info("job finished. checking result files")
            for file in files.values():
                if file.isFetch():
                    self.client.fetchFile(file)
            self.queue.task_done()
