'''
Created on Sep 11, 2009

@author: juanmarcus
'''

class ClientAPI(object):
    def __init__(self, remoteobj):
        self.remoteobj = remoteobj
        
    def runJob(self, job):
        return self.remoteobj.runJob(job)
    
    def runSystemCommand(self, cmd):
        return self.remoteobj.runSystemCommand(cmd)
    
    def setClientConfig(self, config):
        self.remoteobj.setClientConfig(config)
