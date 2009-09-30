from PyQt4 import QtCore, QtGui
from mothership.Controller import Controller
from mothership.interface.MainWindow import MainWindow
from mothership.ControllerAPI import ControllerAPI
import sys

#create app
app = QtGui.QApplication(sys.argv)

#create the controller
controller = Controller()

#create the controller api
api = ControllerAPI(controller)

#create main window
window = MainWindow()
window.show()

#connect window signals to api slots
window.connect(window, QtCore.SIGNAL("startAllNodes"), api.startAllNodes)
window.connect(window, QtCore.SIGNAL("stopAllNodes"), api.stopAllNodes)
window.connect(window, QtCore.SIGNAL("installAgent"), api.installAgent)
window.connect(window, QtCore.SIGNAL("removeAgent"), api.removeAgent)
window.connect(window, QtCore.SIGNAL("createPackage"), api.createPackage)

#start the application
app.exec_()