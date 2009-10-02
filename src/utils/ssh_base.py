'''
Created on Oct 2, 2009

@author: juanmarcus
'''
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