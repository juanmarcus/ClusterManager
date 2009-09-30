'''
Created on Sep 14, 2009

@author: juanmarcus
'''

from threading import Thread

class Send(Thread):
    def __init__(self, node, file):
        self.node = node
        self.file = file
        Thread.__init__(self)
        
    def run(self):
        path = self.file.getServerPath()
        sendFileSSH(self.node, path, self.node.info.workingdir)
        print self.file.name, "not set"
        remotemanager = self.node.getRemoteManager()
        remotemanager.addFile(self.file.name)
        print remotemanager
        print self.file.name, "set"
        
from mothership.file.ManagedFile import ManagedFile
from utils.ssh_utils import sendFileSSH, fetchFileSSH, removeFileSSH
import logging
import os.path
import thread

class FileManager(object):
    def __init__(self):
        self.logger = logging.getLogger("FileManager")
        self.logger.debug("initializing")
        self.files = {}
        self.remotefiles = {}
        self.threads = []
    
    def addFile(self, **args):
        path = args.get("path")
        _, name = os.path.split(path)
        if not name:
            self.logger.error("path is a directory")
            return None
        if self.files.has_key(name):
            self.logger.error("file already managed: %s", name)
            return None
        else:
            autoSend = args.get("autoSend", True)
            if autoSend:
                if not os.path.exists(path):
                    self.logger.error("path wrong or not specified for file: %s" % name)
                    return None
            else:
                self.logger.info("not checking path for file: %s" % name)
                
            self.logger.info("adding file: %s" % name)
            file = ManagedFile(name, **args)
            self.files[name] = file
            return file
        
    def getFile(self, name):
        return self.files[name]

    def sendFile(self, node, file):
        '''
        Send a file to a node.
        '''
        clientname = node.info.name
        if self.remotefiles.has_key(clientname):
            if file.name in self.remotefiles[clientname]:
                return
            else:
                self.remotefiles[clientname].append(file.name)
                self.__send(node, file)
        else:
            self.remotefiles[clientname] = [file.name]
            self.__send(node, file)

    def __send(self, node, file):
        self.logger.info("sending file: %s" % file.name)
        t = Send(node, file)
        self.threads.append(t)
        t.start()

    def fetchFile(self, node, file):
        self.logger.info("fetching file: %s" % file.name)
        thread.start_new_thread(fetchFileSSH, (node, file.name, file.getServerPath()))
        
    def removeFile(self, node, file):
        self.logger.info("removing file: %s" % file.name)
        removeFileSSH(node, file.name)
