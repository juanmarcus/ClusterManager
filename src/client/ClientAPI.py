'''
Created on Sep 16, 2009

@author: Juan Ibiapina
'''

class ClientAPI(object):

    def turnOnMonitor(self):
        pass
            
    def runJob(self, job):
        cmd = job.getCommand()
        return job.files
