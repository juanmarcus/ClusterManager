from mothership.client.ClientAPI import ClientAPI
from utils.ssh_utils import startAgent, stopAgent, sendFileSSH, fetchFileSSH, \
    removeFileSSH
import Pyro.core
import logging
import time

class ClientHandler(object):
    def __init__(self, info):
        self.logger = logging.getLogger("Client:%s" % info.name)
        self.logger.debug("initializing")
        self.info = info
        self.clientapi = None

    def getClientAPI(self):
        return self.clientapi    
    
    def getInfo(self):
        return self.info
    
    def start(self):
        startAgent(self)
        time.sleep(2)
        remoteobj = Pyro.core.getProxyForURI("PYRONAME://:Default.%s" % self.info.name)
        self.clientapi = ClientAPI(remoteobj)
    
    def stop(self):
        stopAgent(self)
    
    def sendFile(self, file):
        path = file.getServerPath()
        sendFileSSH(self, path, self.info.workingdir)
        
    def fetchFile(self, file):
        fetchFileSSH(self, file.name, file.getServerPath())
        
    def removeFile(self, file):
        removeFileSSH(self, file.name)
        
