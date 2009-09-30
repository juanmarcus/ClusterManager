from mothership.config.ConfigProxy import ConfigProxy
from mothership.file.FileManager import FileManager
from mothership.job.JobManager import JobManager
from mothership.node.NodeManager import NodeManager
from mothership.run.Runner import Runner
from utils.module_utils import load_module
import logging
import sys

class Controller(object):
    def __init__(self, configfile="config/config.py"):
        # Create file logger
        LOG_FILENAME = "./log.txt"
        logging.basicConfig(filename=LOG_FILENAME, filemode="w", level=logging.DEBUG)
        
        # Create console logger
        console = logging.StreamHandler(sys.stdout)
        console.setLevel(logging.INFO)
        formatter = logging.Formatter('%(name)-13s: %(levelname)-8s %(message)s')
        console.setFormatter(formatter)
        logging.getLogger('').addHandler(console)
        
        # Initialize
        self.logger = logging.getLogger("Controller")
        self.logger.debug("initializing")
        self.configfile = configfile
        self.nodemanager = NodeManager()

        self.jobmanager = JobManager()
        self.filemanager = FileManager()
        
        # Read configuration file
        self.readConfig()
    
    def stop(self):
        self.nodemanager.stopAllNodes()
        logging.shutdown()

    def getNodeManager(self):
        return self.nodemanager
    
    def getJobManager(self):
        return self.jobmanager
    
    def getFileManager(self):
        return self.filemanager
        
    def readConfig(self):
        self.logger.info("parsing config file: %s" % self.configfile)
        configmodule = load_module(self.configfile)
        configmodule.config(ConfigProxy(self))
        
    def runAllJobs(self):
        runner = Runner(self)
        runner.runAllJobs()
