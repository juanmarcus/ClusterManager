'''
Created on Sep 27, 2009

@author: Juan Ibiapina
'''
import Pyro.core
from node.LocalFileManager import LocalFileManager
from node.LocalWorker import LocalWorker

class NodeManager(object):

    def init(self, daemon):
        self.daemon = daemon
        self.localfilemanager = LocalFileManager()
    
    def createWorker(self):
        localworker = LocalWorker()
        localworker.setLocalFileManager(self.localfilemanager)
        base = Pyro.core.ObjBase()
        base.delegateTo(localworker)
        uri = self.daemon.connect(base)
#        proxy = Pyro.core.getProxyForURI(uri)
        return uri
    
    def addFile(self, name):
        self.localfilemanager.addFile(name)
