import Pyro.core
from mothership.client.ClientAPI import ClientAPI
from utils.system_utils import run_command
import time
import os
import logging

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
        self.startAgent()
        time.sleep(2)
        remoteobj = Pyro.core.getProxyForURI("PYRONAME://:Default.%s" % self.info.name)
        self.clientapi = ClientAPI(remoteobj)
    
    def stop(self):
        self.stopAgent()
    
    def makeSSHBaseCommand(self):
        parts = []
        parts.append("ssh")
        if self.info.username:
            parts.append("-l %s" % self.info.username)
        parts.append("%s" % self.info.name)
        return parts
    
    def makeSSHCommand(self, cmd):
        parts = self.makeSSHBaseCommand()
        parts.append(cmd)
        return " ".join(parts)
    
    def runSSHCommand(self, cmd, waitForResult=False):
        fullcmd = self.makeSSHCommand(cmd)
        self.logger.debug("running ssh command: %s" % fullcmd)
        if waitForResult:
            result = run_command(fullcmd)
        else:
            os.system(fullcmd)
            result = True
        return result
    
    def checkAgent(self):
        self.logger.info("checking for agent")
        result = self.runSSHCommand("ls '%sclient.py' 2>/dev/null" % self.info.clientpath, True)
        if result:
            self.logger.info("agent found")
        else:
            self.logger.info("agent not found")
        return result
    
    def startAgent(self):
        self.logger.info("starting agent")
        cmd = '"DISPLAY=:%s python %sclient.py" &' % (self.info.display, self.info.clientpath)
        self.runSSHCommand(cmd)
    
    def stopAgent(self):
        self.logger.info("stopping agent")
        cmd = '"DISPLAY=:%s killall python" &' % (self.info.display)
        self.runSSHCommand(cmd)
    
    def installAgent(self):
        self.logger.info("creating dir: %s" % self.info.clientpath)
        self.runSSHCommand("mkdir %s" % self.info.clientpath)
        self.sendFileSSH("clientpackage.tar.gz")
        self.logger.info("installing agent")
        self.runSSHCommand('"cd %s; tar -xzf %s"' % (self.info.clientpath, "clientpackage.tar.gz"))
    
    def removeAgent(self):
        self.logger.info("removing agent")
        self.runSSHCommand("rm -rf %s" % self.info.clientpath)

    def sendFile(self, file):
        path = file.getServerPath()
        self.sendFileSSH(path)
        
    def fetchFile(self, file):
        self.fetchFileSSH(file.name, file.getServerPath())
        
    def removeFile(self, file):
        self.removeFileSSH(file.name)

    def removeFileSSH(self, filename):
        self.runSSHCommand('"cd %s; rm %s"' % (self.info.workingdir, filename))
        
    def sendFileSSH(self, filename):
        parts = []
        parts.append("scp")
        parts.append(filename)
        if self.info.username:
            parts.append("%s@%s:%s" % (self.info.username, self.info.name, self.info.workingdir))
        else:
            parts.append("%s:%s" % (self.info.name, self.info.workingdir))
        os.system(" ".join(parts))

    def fetchFileSSH(self, remotefilename, localpath):
        parts = []
        parts.append("scp")
        dest = os.path.join(self.info.workingdir, remotefilename)
        if self.info.username:
            parts.append("%s@%s:%s" % (self.info.username, self.info.name, dest))
        else:
            parts.append("%s:%s" % (self.info.name, dest))
        parts.append(localpath)
        os.system(" ".join(parts))
        
