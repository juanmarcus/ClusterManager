'''
Created on Sep 11, 2009

@author: Juan Ibiapina
'''
import logging

class JobManager(object):
    def __init__(self):
        self.logger = logging.getLogger("JobManager")
        self.logger.info("initializing")
        self.jobs = []
    
    def addJob(self, job):
        self.logger.info("adding job")
        self.jobs.append(job)
        return job

    def getJobList(self):
        return self.jobs