'''
Created on Sep 16, 2009

@author: Juan Ibiapina
'''
class ClientInfo(object):
    '''
    Holds configuration for a client.
    '''
    def __init__(self, name):
        self.name = name
        self.username = None
        self.display = "0"
        self.clientpath = ".cmanager/"
        self.workingdir = "."
        self.workload = 1

    def setWorkload(self, load):
        self.workload = load

    def setClientPath(self, path):
        if not path.endswith("/"):
            path = path + "/"
        self.clientpath = path
        
    def setUserName(self, username):
        self.username = username
        
    def setDisplay(self, display):
        self.display = display    
        
    def setWorkingDir(self, path):
        self.workingdir = path
        
    def getWorkload(self):
        return self.workload
        
    def getName(self):
        return self.name
    
    def getUserName(self):
        return self.username
    
    def getDisplay(self):
        return self.display
    
    def getClientPath(self):
        return self.clientpath
    
    def getWorkingDir(self):
        return self.workingdir
