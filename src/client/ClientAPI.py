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
        os.chdir("./.cmanager")
        
        #run commands in order
        commands = job.getCommands()
        outputs = []
        for cmd in commands:
            result = self.runSystemCommand(cmd)
            outputs.append(result)
            
        os.chdir("..")
        return True

    def setClientInfo(self, info):
        self.info = info