'''
Created on Sep 14, 2009

@author: Juan Ibiapina
'''

class Job():
    '''
    Contains a list of commands and an associated set of input and output files.
    '''
    def __init__(self, name):
        self.files = {}
        self.commands = []
        self.name = name
    
    def getName(self):
        return self.name
    
    def getCommands(self):
        return self.commands
    
    def addFile(self, file):
        self.files[file.getName()] = file
        
    def addCommand(self, cmd):
        self.commands.append(cmd)
        
    def getFiles(self):
        return self.files