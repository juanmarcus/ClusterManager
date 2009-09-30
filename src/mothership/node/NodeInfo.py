'''
Created on Sep 16, 2009

@author: Juan Ibiapina
'''
class NodeInfo(object):
    '''
    Holds configuration for a node.
    '''
    def __init__(self, name):
        self.name = name
        self.username = None
        self.display = "0"
        self.agentpath = ".cmanager/"
        self.workingdir = "."
        self.workload = 1

    def setWorkload(self, load):
        self.workload = load

    def setAgentPath(self, path):
        if not path.endswith("/"):
            path = path + "/"
        self.agentpath = path
        
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
    
    def getAgentPath(self):
        return self.agentpath
    
    def getWorkingDir(self):
        return self.workingdir
