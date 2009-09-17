from PyQt4 import QtCore, QtGui
from mothership.Controller import Controller
from mothership.interface.MainWindow import MainWindow
from mothership.scripting.ScriptAPI import ScriptAPI
import sys

#create app
app = QtGui.QApplication(sys.argv)

#create the controller
controller = Controller()

#create the controller api
api = ScriptAPI(controller)

#create main window
window = MainWindow()
window.show()

#connect window signals to api slots
window.connect(window, QtCore.SIGNAL("startClient"), api.startClient)
window.connect(window, QtCore.SIGNAL("stopClient"), api.stopClient)
window.connect(window, QtCore.SIGNAL("installAgent"), api.installAgent)
window.connect(window, QtCore.SIGNAL("removeAgent"), api.removeAgent)
window.connect(window, QtCore.SIGNAL("turnOnMonitor"), api.turnOnMonitor)
window.connect(window, QtCore.SIGNAL("turnOffMonitor"), api.turnOffMonitor)

#create a callback object and connect to the interface
#TODO

#start the application
app.exec_()