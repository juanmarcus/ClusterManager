'''
Created on Sep 11, 2009

@author: Juan Ibiapina
'''
from Pyro.errors import NamingError
from node.NodeManager import NodeManager
import socket
import Pyro.core
import Pyro.naming

# Enable mobile code and multi thread server
Pyro.config.PYRO_MOBILE_CODE = 1
Pyro.config.PYRO_MULTITHREADED = 1

# Initialize server
Pyro.core.initServer()
ns = Pyro.naming.NameServerLocator().getNS()
daemon = Pyro.core.Daemon()
daemon.useNameServer(ns)

# Create remote manager
remoteManager = NodeManager()
remoteManager_base = Pyro.core.ObjBase()
remoteManager_base.delegateTo(remoteManager)
remoteManager.init(daemon)

# Create object name using hostname
objname = socket.gethostname().lower()

# Unregister the name
try:
    ns.unregister(objname)
except NamingError:
    pass

# Register the name
uri = daemon.connect(remoteManager_base, objname)

# Request loop
daemon.requestLoop()
