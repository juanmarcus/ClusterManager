'''
Created on Sep 11, 2009

@author: Juan Ibiapina
'''
from mothership.job.Job import Job
import logging

class JobManager(object):
    def __init__(self):
        self.logger = logging.getLogger("JobManager")
        self.logger.debug("initializing")
        self.jobs = []
    
    def createJob(self, jobname):
        self.logger.info("creating job: %s" % jobname)
        job = Job(jobname)
        self.jobs.append(job)
        return job

    def getJobList(self):
        return self.jobs
