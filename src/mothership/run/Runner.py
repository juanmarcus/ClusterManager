'''
Created on Sep 14, 2009

@author: Juan Ibiapina
'''
from Queue import Queue
from mothership.run.Worker import Worker
import logging

class Runner(object):
    def __init__(self, controller):
        self.logger = logging.getLogger("Runner")
        self.logger.debug("initializing")
        self.controller = controller
        self.jobmanager = self.controller.getJobManager()
        self.clientmanager = self.controller.getClientManager()
        
    def runAllJobs(self):
        self.logger.info("starting workers")
        joblist = self.jobmanager.getJobList()
        clients = self.clientmanager.getClients()
        
        #creates a queue of jobs
        self.queue = Queue()
        for job in joblist:
            self.queue.put(job)
        
        #creates workers for each client and start them
        self.workers = []
        for client in clients.values():
            worker = Worker(client, self.queue)
            self.workers.append(worker)
            worker.start()
            
        #wait for all workers to finish
        self.logger.info("waiting for completion")
        self.queue.join()
        self.logger.info("all jobs completed")
            
        
