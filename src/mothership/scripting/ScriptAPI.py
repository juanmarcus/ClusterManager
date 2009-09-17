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

    def addJob(self, job):
        rjob = self.jobmanager.addJob(job)
        if not rjob:
            if self.callback:
                self.callback.error("Error adding job. Check log for details.")
        return rjob 
    
    def addFile(self, name, **args):
        file = self.filemanager.addFile(name, **args)
        if not file:
            if self.callback:
                self.callback.error("Error adding file %s. Check log for details." % name)
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
