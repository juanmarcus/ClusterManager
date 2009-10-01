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
        self.data = {}
#        self.localfilemanager = LocalFileManager()
#        self.workers = []
    
    def createWorker(self, id):
        self.logger.info("creating local worker: %s" % id)
        localworker = LocalWorker()
        base = Pyro.core.ObjBase()
        base.delegateTo(localworker)
        self.daemon.connect(base)
        proxy = base.getProxy()
        if self.data.has_key(id):
            self.data[id]["workers"].append(proxy)
        else:
            self.data[id] = {}
            self.data[id]["workers"] = [proxy]
            self.data[id]["filemanager"] = LocalFileManager()
        localworker.setLocalFileManager(self.data[id]["filemanager"])
        return proxy
    
    def addFile(self, name, id):
        self.logger.info("registering file transfer completion: %s" % name)
        self.data[id]["filemanager"].addFile(name)
        
    def stop(self, id):
        if self.data.has_key(id):
            self.data[id]["filemanager"].clean()
            self.data[id]["filemanager"] = None
            self.logger.info("disconnecting all workers with id: %s" % id)
            for proxy in self.data[id]["workers"]:
                self.daemon.disconnect(proxy)
                del proxy
