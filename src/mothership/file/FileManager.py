'''
Created on Sep 14, 2009

@author: juanmarcus
'''
import os.path
from mothership.file.ManagedFile import ManagedFile
from utils.dict_utils import safeGetValue
import logging

class FileManager(object):
    def __init__(self):
        self.logger = logging.getLogger("FileManager")
        self.logger.info("initializing")
        self.files = {}
    
    def addFile(self, name, **args):
        if self.files.has_key(name):
            self.logger.error("file already managed: %s", name)
            return None
        else:
            existing = safeGetValue(args, "existing", True)
            path = safeGetValue(args, "path", "")
            if existing and not os.path.exists(path):
                self.logger.error("path wrong or not specified for file: %s" % name)
                return None
            file = ManagedFile(name, **args)
            if existing:
                file.addInstance(":server", path)
            self.logger.info("adding file: %s" % name)
            self.files[name] = file
            return file
        
    def getFile(self, name):
        return self.files[name]