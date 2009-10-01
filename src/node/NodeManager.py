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
    
    def createWorker(self):
        self.logger.info("creating local worker")
        localworker = LocalWorker()
        localworker.setLocalFileManager(self.localfilemanager)
        base = Pyro.core.ObjBase()
        base.delegateTo(localworker)
        self.daemon.connect(base)
        return base.getProxy()
    
    def addFile(self, name):
        self.logger.info("registering file transfer completion: %s" % name)
        self.localfilemanager.addFile(name)
