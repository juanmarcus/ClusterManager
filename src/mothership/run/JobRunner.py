'''
Created on Sep 16, 2009

@author: Juan Ibiapina
'''
from threading import Thread
from utils.re_utils import listTokens
import logging

class JobRunner(Thread):
    def __init__(self, controller, client, queue):
        Thread.__init__(self)
        self.logger = logging.getLogger("JobRunner:%s"%client.getName())
        self.controller = controller
        self.filemanager = self.controller.getFileManager()
        self.client = client
        self.queue = queue
        
    def run(self):
        while not self.queue.empty():
            #get job
            job = self.queue.get()
            #get command
            cmd = job.getCommand()
            #get tokens
            tokens = listTokens(cmd)
            #check files and send to client
            for filename in tokens:
                file = self.filemanager.getFile(filename)
                if file.exists():
                    self.client.sendFile(file)
                    job.addFile(file)
            #send job to client
            result = self.client.getClientAPI().runJob(job)
            if not result:
                self.logger.error("problem!!")
            self.queue.task_done()