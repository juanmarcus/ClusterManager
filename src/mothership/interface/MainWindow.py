from PyQt4 import QtGui, QtCore

class MainWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        
        #configure layout
        self.mainLayout = QtGui.QVBoxLayout()
        self.setLayout(self.mainLayout)
        
        #file list
#        self.filelist = QtGui.QListWidget()
#        self.mainLayout.addWidget(self.filelist)
        
        #host list
#        self.hostlist = QtGui.QListWidget()
#        self.mainLayout.addWidget(self.hostlist)
        
        #module list
#        self.modulelist = QtGui.QListWidget()
#        self.mainLayout.addWidget(self.modulelist)
        
        #start button
        button = QtGui.QPushButton("Start")
        self.mainLayout.addWidget(button)
        self.connect(button, QtCore.SIGNAL("clicked()"), self.startClients)
        
        #stop button
        button = QtGui.QPushButton("Stop")
        self.mainLayout.addWidget(button)
        self.connect(button, QtCore.SIGNAL("clicked()"), self.stopClients)
        
        #install agent
        button = QtGui.QPushButton("Install agent")
        self.mainLayout.addWidget(button)
        self.connect(button, QtCore.SIGNAL("clicked()"), self.installAgent)
        
        #remove agent
        button = QtGui.QPushButton("Remove agent")
        self.mainLayout.addWidget(button)
        self.connect(button, QtCore.SIGNAL("clicked()"), self.removeAgent)
        
    def installAgent(self):
        self.emit(QtCore.SIGNAL("installAgent"), ":all")
            
    def removeAgent(self):
        self.emit(QtCore.SIGNAL("removeAgent"), ":all")
        
    def startClients(self):
        self.emit(QtCore.SIGNAL("startClient"), ":all")
        
    def stopClients(self):
        self.emit(QtCore.SIGNAL("stopClient"), ":all")
        
if __name__ == "__main__":
    import sys
    from PyQt4 import QtGui
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
