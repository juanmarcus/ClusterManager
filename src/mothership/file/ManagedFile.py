'''
Created on Sep 16, 2009

@author: Juan Ibiapina
'''
from utils.dict_utils import safeGetValue

class ManagedFile(object):
    def __init__(self, name, **args):
        self.name = name
        self.existing = safeGetValue(args, "existing", True)
        self.owners = {}

    def addInstance(self, name, path):
        self.owners[name] = path
    
    def getName(self):
        return self.name
    
    def getPath(self, clientname=":server"):
        return self.owners[clientname]
        
    def exists(self):
        return self.existing
