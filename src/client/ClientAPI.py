'''
Created on Sep 16, 2009

@author: Juan Ibiapina
'''
from utils.system_utils import run_command
from client.JobResults import JobResults
import os

class ClientAPI(object):

    def runSystemCommand(self, cmd):
        return run_command(cmd)

    def runJob(self, job):
        # Create object to return results
        results = JobResults()
        
        # Check and change to working directory
        workdir = self.info.getWorkingDir() 
        
        if os.path.exists(workdir):
            os.chdir(workdir)
            
            #run tasks in order
            tasks = job.getTasks()
            for task in tasks:
                returncode, output = self.runSystemCommand(task.getCommandLine())
                results.addTaskResult(returncode, output)
            results.setJobResult(True)
        else:
            results.setJobResult(False)
            results.setJobError("couldn't find working dir")

        #os.chdir("..")
        # Return results
        return results

    def setClientInfo(self, info):
        self.info = info
