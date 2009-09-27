'''
Created on Sep 27, 2009

@author: Juan Ibiapina
'''
from utils.system_utils import run_command
import os

def makeSSHBaseCommand(client):
    parts = []
    parts.append("ssh")
    if client.info.username:
        parts.append("-l %s" % client.info.username)
    parts.append("%s" % client.info.name)
    return parts

def makeSSHCommand(client, cmd):
    parts = makeSSHBaseCommand(client)
    parts.append(cmd)
    return " ".join(parts)

def runSSHCommand(client, cmd, waitForResult=False):
    fullcmd = makeSSHCommand(client, cmd)
#    client.logger.debug("running ssh command: %s" % fullcmd)
    if waitForResult:
        _, output = run_command(fullcmd)
    else:
        os.system(fullcmd)
        output = True
    return output

def checkAgent(client):
#    client.logger.info("checking for agent")
    result = runSSHCommand(client, "ls '%sclient.py' 2>/dev/null" % client.info.clientpath, True)
#    if result:
#        client.logger.info("agent found")
#    else:
#        client.logger.info("agent not found")
    return result

def startAgent(client):
#    client.logger.info("starting agent")
    cmd = '"DISPLAY=:%s python %sclient.py" &' % (client.info.display, client.info.clientpath)
    runSSHCommand(client, cmd)

def stopAgent(client):
#    client.logger.info("stopping agent")
    cmd = '"DISPLAY=:%s killall python" &' % (client.info.display)
    runSSHCommand(client, cmd)

def installAgent(client):
#    client.logger.info("creating dir: %s" % client.info.clientpath)
    runSSHCommand(client, "mkdir %s" % client.info.clientpath)
    sendFileSSH(client, "clientpackage.tar.gz", client.info.clientpath)
#    client.logger.info("installing agent")
    runSSHCommand(client, '"cd %s; tar -xzf %s"' % (client.info.clientpath, "clientpackage.tar.gz"))

def removeAgent(client):
#    client.logger.info("removing agent")
    runSSHCommand(client, "rm -rf %s" % client.info.clientpath)
    
def removeFileSSH(client, filename):
    runSSHCommand(client, '"cd %s; rm %s"' % (client.info.workingdir, filename))
    
def sendFileSSH(client, filename, destdir):
    parts = []
    parts.append("scp")
    parts.append(filename)
    if client.info.username:
        parts.append("%s@%s:%s" % (client.info.username, client.info.name, destdir))
    else:
        parts.append("%s:%s" % (client.info.name, destdir))
    os.system(" ".join(parts))

def fetchFileSSH(client, remotefilename, localpath):
    parts = []
    parts.append("scp")
    dest = os.path.join(client.info.workingdir, remotefilename)
    if client.info.username:
        parts.append("%s@%s:%s" % (client.info.username, client.info.name, dest))
    else:
        parts.append("%s:%s" % (client.info.name, dest))
    parts.append(localpath)
    os.system(" ".join(parts))