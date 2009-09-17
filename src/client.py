'''
Created on Sep 11, 2009

@author: Juan Ibiapina
'''
from Pyro.errors import NamingError
from client.ClientAPI import ClientAPI
import socket
import Pyro.core
import Pyro.naming

#enable mobile code
Pyro.config.PYRO_MOBILE_CODE = 1

#create api object
clientapi = ClientAPI()

client_proxy = Pyro.core.ObjBase()
client_proxy.delegateTo(clientapi)

Pyro.core.initServer()
ns = Pyro.naming.NameServerLocator().getNS()
daemon = Pyro.core.Daemon()
daemon.useNameServer(ns)

objname = socket.gethostname().lower()
try:
    # 'test' is the name by which our object will be known to the outside world
    ns.unregister(objname)
except NamingError:
    pass

uri = daemon.connect(client_proxy, objname)
daemon.requestLoop()
