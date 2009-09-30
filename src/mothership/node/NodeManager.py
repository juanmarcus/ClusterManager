from mothership.node.NodeInfo import NodeInfo
from mothership.node.NodeHandler import NodeHandler
import logging

class NodeManager(object):
    '''
    Manages nodes.
    '''
    def __init__(self):
        self.logger = logging.getLogger("ClientManager")
        self.logger.debug("initializing")
        self.nodes = {}

    def getNodes(self):
        return self.nodes

    def addNode(self, name):
        self.logger.info("adding node: %s" % name)
        info = NodeInfo(name)
        nodeHandler = NodeHandler(info)
        self.nodes[name] = nodeHandler
        return info
    
    def startAllNodes(self):
        for node in self.nodes.values():
            node.start()
            
    def stopAllNodes(self):
        for node in self.nodes.values():
            node.stop()
