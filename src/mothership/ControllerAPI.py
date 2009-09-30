'''
Created on Sep 29, 2009

@author: Juan Ibiapina
'''
from utils.ssh_utils import startAgent, stopAgent, installAgent, removeAgent
from utils.package_utils import build_package

class ControllerAPI(object):
    def __init__(self, controller):
        self.controller = controller
        self.nodemanager = self.controller.getNodeManager()
        
    def startAllNodes(self):
        nodes = self.nodemanager.getNodes()
        for node in nodes.values():
            startAgent(node)
    
    def stopAllNodes(self):
        nodes = self.nodemanager.getNodes()
        for node in nodes.values():
            stopAgent(node)

    def installAgent(self):
        nodes = self.nodemanager.getNodes()
        for node in nodes.values():
            installAgent(node)
    
    def removeAgent(self):
        nodes = self.nodemanager.getNodes()
        for node in nodes.values():
            removeAgent(node)
    
    def createPackage(self):
        infilename = "config/packagefiles.txt"
        packagename = "nodepackage.tar.gz"
    
        filelist = open(infilename)

        build_package(packagename, filelist)
