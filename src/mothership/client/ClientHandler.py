from subprocess import Popen, PIPE
import Pyro.core
from mothership.client.ClientAPI import ClientAPI
import time
import os
import logging

#run a system command and return the result
def run_command(cmd):
    p = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
    out = " ".join(p.stdout.readlines())
    return out

class ClientHandler(object):
    def __init__(self, name):
        self.logger = logging.getLogger("Client:%s" % name)
        self.logger.info("initializing")
        self.name = name
        self.username = None
        self.display = "0"
        self.clientpath = ".cmanager/"
        self.remotename = self.name
        self.clientapi = None

    def setClientPath(self, path):
        if not path.endswith("/"):
            path = path + "/"
        self.logger.info("setting client path: %s" % path)
        self.clientpath = path
        
    def setUserName(self, username):
        self.logger.info("setting user name: %s" % username)
        self.username = username
        
    def setDisplay(self, display):
        self.logger.info("setting display: %s" % display)
        self.display = display    
        
    def getClientAPI(self):
        return self.clientapi    
    
    def getName(self):
        return self.name
    
    def getUserName(self):
        return self.username
    
    def getDisplay(self):
        return self.display
    
    def getClientPath(self):
        return self.clientpath
    
    def start(self):
        self.startAgent()
        time.sleep(2)
        remoteobj = Pyro.core.getProxyForURI("PYRONAME://:Default.%s" % self.remotename)
        self.clientapi = ClientAPI(remoteobj)
    
    def stop(self):
        self.stopAgent()
    
    def makeSSHBaseCommand(self):
        parts = []
        parts.append("ssh")
        if self.username:
            parts.append("-l %s" % self.username)
        parts.append("%s" % self.name)
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
        result = self.runSSHCommand("ls '%sclient.py' 2>/dev/null" % self.clientpath, True)
        if result:
            self.logger.info("client found")
        else:
            self.logger.info("client not found")
        return result
    
    def startAgent(self):
        self.logger.info("starting agent")
        cmd = '"DISPLAY=:%s python %sclient.py" &' % (self.display, self.clientpath)
        self.runSSHCommand(cmd)
    
    def stopAgent(self):
        self.logger.info("stopping agent")
        cmd = '"DISPLAY=:%s killall python" &' % (self.display)
        self.runSSHCommand(cmd)
    
    def turnOnMonitor(self):
        self.logger.info("turning on monitor")
        self.runSSHCommand("DISPLAY=:%s xset dpms force on" % self.display)
        
    def turnOffMonitor(self):
        self.logger.info("turning off monitor")
        self.runSSHCommand("DISPLAY=:%s xset dpms force off" % self.display)
        
    def installAgent(self):
        self.logger.info("creating dir: %s" % self.clientpath)
        self.runSSHCommand("mkdir %s" % self.clientpath)
        self.sendFileSSH("clientpackage.tar.gz")
        self.logger.info("installing agent")
        self.runSSHCommand('"cd %s; tar -xzf %s"' % (self.clientpath, "clientpackage.tar.gz"))
    
    def removeAgent(self):
        self.logger.info("removing agent")
        self.runSSHCommand("rm -rf %s" % self.clientpath)

    def sendFile(self, file):
        path = file.getPath()
        remotepath = self.sendFileSSH(path)
        file.addInstance(self.name, remotepath)

    def sendFileSSH(self, filename, dest=None):
        self.logger.info("sending file: %s" % filename)
        parts = []
        parts.append("scp")
        parts.append(filename)
        if dest:
            dest = os.path.join(self.clientpath, dest)
        else:
            dest = self.clientpath
        self.logger.info("destination: %s" % dest)
        if self.username:
            parts.append("%s@%s:%s" % (self.username, self.name, dest))
        else:
            parts.append("%s:%s" % (self.name, dest))
        os.system(" ".join(parts))
        return os.path.join(dest, filename)
