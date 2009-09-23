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
            job.error("couldn't find work dir")
        
        #run tasks in order
        tasks = job.getTasks()
        for task in tasks:
            result = self.runSystemCommand(task.getCommandLine())
            task.setOutput(result)

#        os.chdir("..")
        return True

    def setClientInfo(self, info):
        self.info = info