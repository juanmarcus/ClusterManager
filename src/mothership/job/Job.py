'''
Created on Sep 14, 2009

@author: Juan Ibiapina
'''
from mothership.job.Task import Task

class Job():
    '''
    Contains a list of commands and an associated set of input and output files.
    '''
    def __init__(self, name):
        self.files = {}
        self.tasks = []
        self.name = name
    
    def getName(self):
        return self.name
    
    def getTasks(self):
        return self.tasks
    
    def addFile(self, file):
        self.files[file.getName()] = file
        
    def addTask(self, cmd, pars = None):
        task = Task(cmd, pars)
        self.tasks.append(task)
        return task
        
    def getFiles(self):
        return self.files