import Pyro.core
import logging

class NodeHandler(object):
    def __init__(self, info):
        self.logger = logging.getLogger("Node:%s" % info.name)
        self.logger.debug("initializing")
        self.info = info
        self.remotemanager = None

    def getClientAPI(self):
        return self.remotemanager    
    
    def getInfo(self):
        return self.info
    
    def start(self):
        self.remotemanager = Pyro.core.getProxyForURI("PYRONAME://:Default.%s" % self.info.name)
            
    def stop(self):
        pass        

    def createRemoteWorker(self):
        uri = self.remotemanager.createWorker()
        remoteworker = Pyro.core.getProxyForURI(uri)
        return remoteworker

    def getRemoteManager(self):
        return self.remotemanager