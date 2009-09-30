'''
Created on Sep 11, 2009

@author: Juan Ibiapina
'''

class ScriptAPI(object):
    def __init__(self, controller):
        self.controller = controller
        self.nodemanager = self.controller.getNodeManager()
        self.jobmanager = self.controller.getJobManager()
        self.filemanager = self.controller.getFileManager()
        self.callback = None

    def setCallback(self, callback):
        self.callback = callback

    def createJob(self, jobname):
        job = self.jobmanager.createJob(jobname)
        if not job:
            if self.callback:
                self.callback.error("Error creating job. Check log for details.")
        return job 
    
    def addFile(self, **args):
        file = self.filemanager.addFile(**args)
        if not file:
            if self.callback:
                self.callback.error("Error adding file %s. Check log for details.")
        return file

    def runAllJobs(self):
        self.controller.runAllJobs()
            
    def startAllNodes(self):
        self.nodemanager.startAllNodes()