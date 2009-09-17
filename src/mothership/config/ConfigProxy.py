class ConfigProxy(object):
    '''
    Contains methods to be called from configuration files.
    '''
    def __init__(self, controller):
        self.controller = controller
        self.clientmanager = controller.getClientManager()
        
    def addClient(self, name):
        return self.clientmanager.addClient(name)