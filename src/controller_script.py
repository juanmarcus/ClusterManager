'''
Created on Sep 14, 2009

@author: juanmarcus
'''
from mothership.Controller import Controller
from mothership.scripting.ScriptAPI import ScriptAPI
from utils.module_utils import load_module
import sys

#check args    
if len(sys.argv) < 2:
    print "missing script name"
    sys.exit(1)
scriptfilename = sys.argv[1]

#create the controller
controller = Controller()

#create the controller api
api = ScriptAPI(controller)

script = load_module(scriptfilename)
script.run(api)

controller.stop()
