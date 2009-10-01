'''
Created on Sep 16, 2009

@author: Juan Ibiapina
'''
from node.JobResults import JobResults
from utils.system_utils import run_command
import logging
import os
import time

class LocalWorker(object):

    def init(self, info):
        self.logger = logging.getLogger("Worker")
        self.logger.debug("initializing")
        self.info = info

    def runJob(self, job):
        self.logger.info("creating JobResults")
        # Create object to return results
        results = JobResults()
        
        self.logger.info("reading working directory")
        # Check and change to working directory
        workdir = self.info.getWorkingDir() 
        
        if os.path.exists(workdir):
            self.logger.info("changing to working directory")
            os.chdir(workdir)
            
            # Wait for files
            self.logger.info("waiting for file tranfers to complete")
            files = [file.getName() for file in job.getFiles().values() if file.hasAutoSend()]
            self.logger.debug("files: %s" % str(files))
            while not self.localfilemanager.hasFiles(files):
                self.logger.debug("files not ready, sleeping")
                time.sleep(1)
            self.logger.info("file transfers completed")
            
            #run tasks in order
            self.logger.info("running tasks")
            tasks = job.getTasks()
            for task in tasks:
                cmdline = task.getCommandLine()
                self.logger.debug("running task: %s" % (cmdline))
                returncode, output = run_command(cmdline)
                self.logger.debug("task: %s\n\treturn code: %s\n\toutput:\n%s" % (cmdline, str(returncode), str(output)))
                results.addTaskResult(returncode, output)
            results.setJobResult(True)
        else:
            self.logger.info("couldn't find working directory")
            results.setJobResult(False)
            results.setJobError("couldn't find working directory")

        #os.chdir("..")
        # Return results
        self.logger.info("returning results")
        return results

    def stop(self):
        self.logger.info("stopping worker")
        # TODO destroy the worker and unregister

    def setLocalFileManager(self, localfilemanager):
        self.localfilemanager = localfilemanager
        
