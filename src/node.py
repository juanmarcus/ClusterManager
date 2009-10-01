'''
Created on Sep 11, 2009

@author: Juan Ibiapina
'''
#from Pyro.errors import NamingError
from node.NodeManager import NodeManager
import Pyro.core
import logging
import socket
import sys
#import Pyro.naming

# Create file logger
LOG_FILENAME = "./node_log.txt"
logging.basicConfig(filename=LOG_FILENAME, filemode="w", level=logging.DEBUG)

# Create console logger
console = logging.StreamHandler(sys.stdout)
console.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(name)-13s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)

# Initialize
logger = logging.getLogger("Node")
logger.debug("initializing")

# Configure some server options
Pyro.config.PYRO_MOBILE_CODE = 0
Pyro.config.PYRO_MULTITHREADED = 1
Pyro.config.PYRO_TRACELEVEL = 3
Pyro.config.PYRO_STDLOGGING = 0
Pyro.config.PYRO_USER_TRACELEVEL = 3


# Initialize server
Pyro.core.initServer()
#ns = Pyro.naming.NameServerLocator().getNS()
daemon = Pyro.core.Daemon()
#daemon.useNameServer(ns)

# Create a node manager
nodeManager = NodeManager()
nodeManager_base = Pyro.core.ObjBase()
nodeManager_base.delegateTo(nodeManager)
nodeManager.init(daemon)

# Create object name using lower case host name
objname = socket.gethostname().lower()
logger.info("name: %s" % objname)

# Unregister the name
#try:
#    ns.unregister(objname)
#except NamingError:
#    pass

# Register the object with the daemon
uri = daemon.connect(nodeManager_base, objname)

# Request loop
daemon.requestLoop()
