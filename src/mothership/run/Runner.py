'''
Created on Sep 14, 2009

@author: Juan Ibiapina
'''
from Queue import Queue
from mothership.run.JobRunner import JobRunner
import logging

class Runner(object):
    def __init__(self, controller):
        self.logger = logging.getLogger("Runner")
        self.logger.info("initializing")
        self.controller = controller
        self.jobmanager = self.controller.getJobManager()
        self.clientmanager = self.controller.getClientManager()
        
    def runAllJobs(self):
        self.logger.info("starting JobRunners")
        joblist = self.jobmanager.getJobList()
        clients = self.clientmanager.getClients()
        
        #creates a queue of jobs
        self.queue = Queue()
        for job in joblist:
            self.queue.put(job)
        
        #creates one JobRunner for each client and start them
        self.runners = []
        for client in clients.values():
            runner = JobRunner(self.controller, client, self.queue)
            self.runners.append(runner)
            runner.start()
            
        #wait for all runners to finish
        self.logger.info("waiting for completion")
        self.queue.join()
            
        
