'''
Created on Sep 25, 2009

@author: Juan Ibiapina
'''

class JobResults(object):
    def __init__(self):
        self.joberror = None
        self.jobresult = None
        self.taskresults = []

    def setJobResult(self, bool):
        self.jobresult = bool

    def setJobError(self, error):
        self.joberror = error

    def addTaskResult(self, code, output):
        self.taskresults.append((code, output))
        
    def getJobResult(self):
        return self.jobresult
    
    def getJobError(self):
        return self.joberror
    
    def getTaskResults(self):
        return self.taskresults
