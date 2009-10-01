import Pyro.core
from datetime import datetime
import socket
import logging

class NodeHandler(object):
    
    @classmethod
    def makeUniqueId(cls):
        dt = datetime.now()
        name = socket.gethostname().lower() + str(dt.microsecond)
        return name
    
    def __init__(self, info):
        self.logger = logging.getLogger("Node:%s" % info.name)
        self.logger.debug("initializing")
        self.info = info
        self.remotemanager = None
        self.uniqueid = self.makeUniqueId()

    def getInfo(self):
        return self.info
    
    def start(self):
        self.logger.info("connecting to remote node")
        self.remotemanager = Pyro.core.getProxyForURI("PYROLOC://%s/%s" % (self.info.name, self.info.name))
            
    def stop(self):
        self.logger.info("stopping remote node")
        self.remotemanager._setOneway("stop")
        self.remotemanager.stop(self.uniqueid)        

    def createRemoteWorker(self):
        self.logger.info("creating remote worker")
        remoteworker = self.remotemanager.createWorker(self.uniqueid)
        return remoteworker

    def getRemoteManager(self):
        return self.remotemanager