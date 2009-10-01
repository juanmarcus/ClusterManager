'''
Created on Sep 27, 2009

@author: Juan Ibiapina
'''
from node.LocalFileManager import LocalFileManager
from node.LocalWorker import LocalWorker
import Pyro.core
import logging

class NodeManager(object):

    def init(self, daemon):
        self.logger = logging.getLogger("NodeManager")
        self.logger.debug("initializing")
        self.daemon = daemon
        self.localfilemanager = LocalFileManager()
        self.workers = []
    
    def createWorker(self):
        self.logger.info("creating local worker")
        localworker = LocalWorker()
        localworker.setLocalFileManager(self.localfilemanager)
        base = Pyro.core.ObjBase()
        base.delegateTo(localworker)
        self.daemon.connect(base)
        proxy = base.getProxy()
        self.workers.append(proxy)
        return proxy
    
    def addFile(self, name):
        self.logger.info("registering file transfer completion: %s" % name)
        self.localfilemanager.addFile(name)
        
    def stop(self):
        self.localfilemanager.clean()
        self.logger.info("disconnecting all workers")
        for proxy in self.workers:
            self.daemon.disconnect(proxy)
            del proxy
        self.workers = []
