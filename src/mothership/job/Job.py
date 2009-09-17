'''
Created on Sep 14, 2009

@author: Juan Ibiapina
'''

class Job():
    def __init__(self, cmd):
        self.files = {}
        self.cmd = cmd
    
    def getCommand(self):
        return self.cmd
    
    def addFile(self, file):
        self.files[file.getName()] = file