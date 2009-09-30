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
        self.nodemanager = self.controller.getNodeManager()
        
    def runAllJobs(self):
        self.logger.info("starting workers")
        joblist = self.jobmanager.getJobList()
        nodes = self.nodemanager.getNodes()
        
        # Create a queue of jobs
        self.queue = Queue()
        for job in joblist:
            self.queue.put(job)
        
        # Create workers for each node and start them
        self.workers = []
        for node in nodes.values():
            worker = Worker(node, self.queue, self.controller)
            self.workers.append(worker)
            worker.start()
            
        # Wait for all jobs to be processed
        self.logger.info("waiting for completion")
        self.queue.join()
        self.logger.info("all jobs completed")
            
        
