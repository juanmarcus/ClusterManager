'''
Created on Sep 14, 2009

@author: juanmarcus
'''
import os.path
from mothership.file.ManagedFile import ManagedFile
import logging

class FileManager(object):
    def __init__(self):
        self.logger = logging.getLogger("FileManager")
        self.logger.debug("initializing")
        self.files = {}
    
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
                
            file = ManagedFile(name, **args)
            self.logger.info("adding file: %s" % name)
            self.files[name] = file
            return file
        
    def getFile(self, name):
        return self.files[name]
