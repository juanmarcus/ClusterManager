import Pyro.core
import logging

class NodeHandler(object):
    def __init__(self, info):
        self.logger = logging.getLogger("Node:%s" % info.name)
        self.logger.debug("initializing")
        self.info = info
        self.remotemanager = None

    def getInfo(self):
        return self.info
    
    def start(self):
        self.remotemanager = Pyro.core.getProxyForURI("PYROLOC://%s/%s" % (self.info.name, self.info.name))
            
    def stop(self):
        pass        

    def createRemoteWorker(self):
        remoteworker = self.remotemanager.createWorker()
        return remoteworker

    def getRemoteManager(self):
        return self.remotemanager