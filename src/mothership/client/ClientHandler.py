from subprocess import Popen, PIPE
import Pyro.core
from mothership.client.ClientAPI import ClientAPI
from utils.system_utils import run_command
import time
import os
import logging

class ClientHandler(object):
    def __init__(self, config):
        self.logger = logging.getLogger("Client:%s" % config.name)
        self.logger.info("initializing")
        self.config = config
        self.clientapi = None

    def getClientAPI(self):
        return self.clientapi    
    
    def getConfig(self):
        return self.config
    
    def start(self):
        self.startAgent()
        time.sleep(2)
        remoteobj = Pyro.core.getProxyForURI("PYRONAME://:Default.%s" % self.config.remotename)
        self.clientapi = ClientAPI(remoteobj)
    
    def stop(self):
        self.stopAgent()
    
    def makeSSHBaseCommand(self):
        parts = []
        parts.append("ssh")
        if self.config.username:
            parts.append("-l %s" % self.config.username)
        parts.append("%s" % self.config.name)
        return parts
    
    def makeSSHCommand(self, cmd):
        parts = self.makeSSHBaseCommand()
        parts.append(cmd)
        return " ".join(parts)
    
    def runSSHCommand(self, cmd, waitForResult=False):
        fullcmd = self.makeSSHCommand(cmd)
        self.logger.info("running ssh command: %s" % fullcmd)
        if waitForResult:
            result = run_command(fullcmd)
        else:
            os.system(fullcmd)
            result = True
        return result
    
    def checkAgent(self):
        self.logger.info("checking for client")
        result = self.runSSHCommand("ls '%sclient.py' 2>/dev/null" % self.config.clientpath, True)
        if result:
            self.logger.info("client found")
        else:
            self.logger.info("client not found")
        return result
    
    def startAgent(self):
        self.logger.info("starting agent")
        cmd = '"DISPLAY=:%s python %sclient.py" &' % (self.config.display, self.config.clientpath)
        self.runSSHCommand(cmd)
    
    def stopAgent(self):
        self.logger.info("stopping agent")
        cmd = '"DISPLAY=:%s killall python" &' % (self.config.display)
        self.runSSHCommand(cmd)
    
    def turnOnMonitor(self):
        self.logger.info("turning on monitor")
        self.runSSHCommand("DISPLAY=:%s xset dpms force on" % self.config.display)
        
    def turnOffMonitor(self):
        self.logger.info("turning off monitor")
        self.runSSHCommand("DISPLAY=:%s xset dpms force off" % self.config.display)
        
    def installAgent(self):
        self.logger.info("creating dir: %s" % self.config.clientpath)
        self.runSSHCommand("mkdir %s" % self.config.clientpath)
        self.sendFileSSH("clientpackage.tar.gz")
        self.logger.info("installing agent")
        self.runSSHCommand('"cd %s; tar -xzf %s"' % (self.config.clientpath, "clientpackage.tar.gz"))
    
    def removeAgent(self):
        self.logger.info("removing agent")
        self.runSSHCommand("rm -rf %s" % self.config.clientpath)

    def sendFile(self, file):
        path = file.getPath()
        remotepath = self.sendFileSSH(path)
        file.addInstance(self.config.name, remotepath)

    def sendFileSSH(self, filename, dest=None):
        self.logger.info("sending file: %s" % filename)
        parts = []
        parts.append("scp")
        parts.append(filename)
        if dest:
            dest = os.path.join(self.config.clientpath, dest)
        else:
            dest = self.config.clientpath
        self.logger.info("destination: %s" % dest)
        if self.config.username:
            parts.append("%s@%s:%s" % (self.config.username, self.config.name, dest))
        else:
            parts.append("%s:%s" % (self.config.name, dest))
        os.system(" ".join(parts))
        return os.path.join(dest, filename)
