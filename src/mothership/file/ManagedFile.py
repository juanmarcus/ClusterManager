'''
Created on Sep 16, 2009

@author: Juan Ibiapina
'''
class ManagedFile(object):
    def __init__(self, name, **args):
        self.name = name
        self.serverpath = args.get("path")
        self.autoFetch = args.get("autoFetch", False)
        self.autoSend = args.get("autoSend", True)
        self.autoRemove = args.get("autoRemove", True)

    def getName(self):
        return self.name
    
    def getServerPath(self):
        return self.serverpath
        
    def hasAutoFetch(self):
        return self.autoFetch
    
    def hasAutoRemove(self):
        return self.autoRemove
    
    def hasAutoSend(self):
        return self.autoSend