'''
Created on Sep 14, 2009

@author: juanmarcus
'''

from threading import Thread

from mothership.file.ManagedFile import ManagedFile
from utils.ssh_utils import sendFileSSH, fetchFileSSH, removeFileSSH
import threading
import thread
import logging
import os.path

class FileManager(object):
    def __init__(self):
        self.logger = logging.getLogger("FileManager")
        self.logger.debug("initializing")
        self.files = {}
        self.remotefiles = {}
        self.lock = threading.Lock()
    
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
        self.lock.acquire()
        if self.remotefiles.has_key(clientname):
            if file.name in self.remotefiles[clientname]:
                pass
            else:
                self.remotefiles[clientname].append(file.name)
                self.__send(node, file)
        else:
            self.remotefiles[clientname] = [file.name]
            self.__send(node, file)
        self.lock.release()

    def __send(self, node, file):
        self.logger.info("sending file: %s" % file.name)
        def send_thread(node, file):
            path = file.getServerPath()
            sendFileSSH(node, path, node.info.workingdir)
            remotemanager = node.getRemoteManager()
            remotemanager.addFile(file.name, node.uniqueid)
        thread.start_new_thread(send_thread, (node, file))

    def fetchFile(self, node, file):
        self.logger.info("fetching file: %s" % file.name)
        fetchFileSSH(node, file.name, file.getServerPath())
        
    def removeFile(self, node, file):
        self.logger.info("removing remote file: %s" % file.name)
        removeFileSSH(node, file.name)
