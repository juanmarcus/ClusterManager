'''
Created on Sep 11, 2009

@author: Juan Ibiapina
'''

class ScriptAPI(object):
    def __init__(self, controller):
        self.controller = controller
        self.clientmanager = self.controller.getClientManager()
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
            
    def startAllClients(self):
        self.clientmanager.startClient(":all")

    def startClient(self, name):
        self.clientmanager.startClient(name)
        
    def stopClient(self, name):
        self.clientmanager.stopClient(name)
        
    def installAgent(self, name = ":all"):
        self.clientmanager.installAgent(name)
        
    def removeAgent(self, name = ":all"):
        self.clientmanager.removeAgent(name)
        
    def turnOnMonitor(self, name = ":all"):
        self.clientmanager.turnOnMonitor(name)
        
    def turnOffMonitor(self, name = ":all"):
        self.clientmanager.turnOffMonitor(name)
