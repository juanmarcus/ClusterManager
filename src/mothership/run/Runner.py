'''
Created on Sep 14, 2009

@author: juanmarcus
'''
from Queue import Queue
from mothership.run.JobRunner import JobRunner

class Runner(object):
    def __init__(self, controller):
        self.controller = controller
        self.jobmanager = self.controller.getJobManager()
        self.clientmanager = self.controller.getClientManager()
        
    def runAllJobs(self):
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
        self.queue.join()
            
        
