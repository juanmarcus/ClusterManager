from mothership.client.ClientHandler import ClientHandler
from mothership.client.ClientInfo import ClientInfo
import logging

class ClientManager(object):
    '''
    Manages clients and connections to the server.
    '''
    def __init__(self):
        self.logger = logging.getLogger("ClientManager")
        self.logger.info("initializing")
        self.clients = {}

    def getClients(self):
        return self.clients

    def addClient(self, name):
        self.logger.info("adding client %s" % name)
        info = ClientInfo(name)
        client = ClientHandler(info)
        self.clients[name] = client
        return info

    def startClient(self, name):
        if name == ":all":
            self.logger.info("trying to start all clients")
            for client in self.clients.values():
                if not client.checkAgent():
                    client.removeAgent()
                    client.installAgent()
                client.start()
        else:
            if self.clients.has_key(name):
                self.logger.info("trying to start client %s" % name)
                client = self.clients[name]
                if not client.checkAgent():
                    client.removeAgent()
                    client.installAgent()
                client.start()
            else:
                self.logger.warning("client %s not configured" % name)
                
    def stopClient(self, name):
        if name == ":all":
            self.logger.info("trying to stop all clients")
            for client in self.clients.values():
                client.stop()
        else:
            if self.clients.has_key(name):
                self.logger.info("trying to stop client %s" % name)
                client = self.clients[name]
                client.stop()
            else:
                self.logger.warning("client %s not configured" % name)
                
    def installAgent(self, name):
        if name == ":all":
            self.logger.info("trying to install agent on all clients")
            for client in self.clients.values():
                client.installAgent()
        else:
            if self.clients.has_key(name):
                self.logger.info("trying to install agent on client %s" % name)
                client = self.clients[name]
                client.installAgent()
            else:
                self.logger.warning("client %s not configured" % name)
                
    def removeAgent(self, name):
        if name == ":all":
            self.logger.info("trying to remove agent from all clients")
            for client in self.clients.values():
                client.removeAgent()
        else:
            if self.clients.has_key(name):
                self.logger.info("trying to remove agent from client %s" % name)
                client = self.clients[name]
                client.removeAgent()
            else:
                self.logger.warning("client %s not configured" % name)

    def turnOnMonitor(self, name):
        if name == ":all":
            self.logger.info("trying to turn on all monitors")
            for host in self.clients.values():
                host.turnOnMonitor()
        else:
            if self.clients.has_key(name):
                self.logger.info("trying to turn on monitor on %s" % name)
                host = self.clients[name]
                host.turnOnMonitor()
            else:
                self.logger.warning("client %s not configured" % name)
                
    def turnOffMonitor(self, name):
        if name == ":all":
            self.logger.info("trying to turn off all monitors")
            for host in self.clients.values():
                host.turnOffMonitor()
        else:
            if self.clients.has_key(name):
                self.logger.info("trying to turn off monitor on %s" % name)
                host = self.clients[name]
                host.turnOffMonitor()
            else:
                self.logger.warning("client %s not configured" % name)