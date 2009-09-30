class ConfigProxy(object):
    '''
    Contains methods to be called from configuration files.
    '''
    def __init__(self, controller):
        self.nodemanager = controller.getNodeManager()
        
    def addNode(self, name):
        return self.nodemanager.addNode(name)