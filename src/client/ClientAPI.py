'''
Created on Sep 16, 2009

@author: Juan Ibiapina
'''
from utils.system_utils import run_command
import os

class ClientAPI(object):

    def runSystemCommand(self, cmd):
        return run_command(cmd)

    def runJob(self, job):
        #check and change to working dir
        workdir =self.info.getWorkingDir() 
        if os.path.exists(workdir):
            os.chdir(workdir)
        else:
            job.setError("couldn't find working dir")
            return False
        
        #run tasks in order
        tasks = job.getTasks()
        for task in tasks:
            returncode, output = self.runSystemCommand(task.makeCommand())
            if not output == None:
                task.setOutput(output)
            if not returncode == None:
                task.setReturnCode(returncode)

#        os.chdir("..")
        return True

    def setClientInfo(self, info):
        self.info = info
