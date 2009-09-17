from mothership.client.ClientManager import ClientManager
from mothership.job.JobManager import JobManager
from mothership.file.FileManager import FileManager
from mothership.config.ConfigProxy import ConfigProxy
from utils.module_utils import load_module
from mothership.run.Runner import Runner
import sys
import logging

class Controller(object):
    def __init__(self, configfile="config/config.py"):
        #create file logger
        LOG_FILENAME = "./log.txt"
        logging.basicConfig(filename=LOG_FILENAME, filemode="w", level=logging.DEBUG)
        
        #create console logger
        console = logging.StreamHandler(sys.stdout)
        console.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
        console.setFormatter(formatter)
        logging.getLogger('').addHandler(console)
        
        #initialize
        self.logger = logging.getLogger("Controller")
        self.logger.info("initializing")
        self.configfile = configfile
        self.clientmanager = ClientManager()
        self.jobmanager = JobManager()
        self.filemanager = FileManager()
        self.readConfig()
    
    def stop(self):
        self.clientmanager.stopClient(":all")
        logging.shutdown()

    def getClientManager(self):
        return self.clientmanager
    
    def getJobManager(self):
        return self.jobmanager
    
    def getFileManager(self):
        return self.filemanager
        
    def readConfig(self):
        self.logger.info("parsing config file %s" % self.configfile)
        configmodule = load_module(self.configfile)
        configmodule.config(ConfigProxy(self))
        
    def runAllJobs(self):
        runner = Runner(self)
        runner.runAllJobs()
        
#    def addFile(self, filename):
#        mfile = self.filemanager.addFile(filename)
#        if mfile:
#            self.emit(QtCore.SIGNAL("fileAdded"), mfile.getName())
#    
#    def sendFile(self, filename, hostname):
#        if self.clients.has_key(hostname):
#            host = self.clients[hostname]
#            file = self.filemanager.getFile(filename)
#            if file:
#                host.sendFile(file)
#            else:
#                self.logger.error("file %s not configured" % filename)
#        else:
#            self.logger.error("host %s not configured" % hostname)
            
            
            
            
            















            
