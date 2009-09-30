'''
Created on Sep 27, 2009

@author: Juan Ibiapina
'''
from utils.system_utils import run_command
import os

def makeSSHBaseCommand(node):
    parts = []
    parts.append("ssh")
    if node.info.username:
        parts.append("-l %s" % node.info.username)
    parts.append("%s" % node.info.name)
    return parts

def makeSSHCommand(node, cmd):
    parts = makeSSHBaseCommand(node)
    parts.append(cmd)
    return " ".join(parts)

def runSSHCommand(node, cmd, waitForResult=False):
    fullcmd = makeSSHCommand(node, cmd)
#    node.logger.debug("running ssh command: %s" % fullcmd)
    if waitForResult:
        _, output = run_command(fullcmd)
    else:
        os.system(fullcmd)
        output = True
    return output

def checkAgent(node):
#    node.logger.info("checking for agent")
    result = runSSHCommand(node, "ls '%snode.py' 2>/dev/null" % node.info.agentpath, True)
#    if result:
#        node.logger.info("agent found")
#    else:
#        node.logger.info("agent not found")
    return result

def startAgent(node):
#    node.logger.info("starting agent")
    cmd = '"DISPLAY=:%s python %snode.py" &' % (node.info.display, node.info.agentpath)
    runSSHCommand(node, cmd)

def stopAgent(node):
#    node.logger.info("stopping agent")
    cmd = '"DISPLAY=:%s killall python" &' % (node.info.display)
    runSSHCommand(node, cmd)

def installAgent(node):
#    node.logger.info("creating dir: %s" % node.info.agentpath)
    runSSHCommand(node, "mkdir %s" % node.info.agentpath)
    sendFileSSH(node, "nodepackage.tar.gz", node.info.agentpath)
#    node.logger.info("installing agent")
    runSSHCommand(node, '"cd %s; tar -xzf %s"' % (node.info.agentpath, "nodepackage.tar.gz"))

def removeAgent(node):
#    node.logger.info("removing agent")
    runSSHCommand(node, "rm -rf %s" % node.info.agentpath)
    
def removeFileSSH(node, filename):
    runSSHCommand(node, '"cd %s; rm %s"' % (node.info.workingdir, filename))
    
def sendFileSSH(node, filename, destdir):
    parts = []
    parts.append("scp")
    parts.append(filename)
    if node.info.username:
        parts.append("%s@%s:%s" % (node.info.username, node.info.name, destdir))
    else:
        parts.append("%s:%s" % (node.info.name, destdir))
    os.system(" ".join(parts))

def fetchFileSSH(node, remotefilename, localpath):
    parts = []
    parts.append("scp")
    dest = os.path.join(node.info.workingdir, remotefilename)
    if node.info.username:
        parts.append("%s@%s:%s" % (node.info.username, node.info.name, dest))
    else:
        parts.append("%s:%s" % (node.info.name, dest))
    parts.append(localpath)
    os.system(" ".join(parts))