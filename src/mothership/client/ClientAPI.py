'''
Created on Sep 11, 2009

@author: juanmarcus
'''

class ClientAPI(object):
    def __init__(self, remoteobj):
        self.remoteobj = remoteobj
        
    def turnOnMonitor(self):
        self.remoteobj.turnOnMonitor()
        
    def runJob(self, job):
        return self.remoteobj.runJob(job)