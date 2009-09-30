'''
Created on Sep 16, 2009

@author: Juan Ibiapina
'''
from node.JobResults import JobResults
from utils.system_utils import run_command
import time
import os

class LocalWorker(object):

    def runJob(self, job):
        # Create object to return results
        results = JobResults()
        
        # Check and change to working directory
        workdir = self.info.getWorkingDir() 
        
        if os.path.exists(workdir):
            os.chdir(workdir)
            
            # Wait for files
            files = [file.getName() for file in job.getFiles().values() if file.hasAutoSend()]
            while not self.localfilemanager.hasFiles(files):
                time.sleep(1)
            
            #run tasks in order
            tasks = job.getTasks()
            for task in tasks:
                returncode, output = run_command(task.getCommandLine())
                results.addTaskResult(returncode, output)
            results.setJobResult(True)
        else:
            results.setJobResult(False)
            results.setJobError("couldn't find working dir")

        #os.chdir("..")
        # Return results
        return results

    def setNodeInfo(self, info):
        self.info = info

    def setLocalFileManager(self, localfilemanager):
        self.localfilemanager = localfilemanager
        
