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
        button = QtGui.QPushButton("Start Nodes")
        self.mainLayout.addWidget(button)
        self.connect(button, QtCore.SIGNAL("clicked()"), self.startAllNodes)
        
        #stop button
        button = QtGui.QPushButton("Stop Nodes")
        self.mainLayout.addWidget(button)
        self.connect(button, QtCore.SIGNAL("clicked()"), self.stopAllNodes)
        
        #install agent
        button = QtGui.QPushButton("Install agent")
        self.mainLayout.addWidget(button)
        self.connect(button, QtCore.SIGNAL("clicked()"), self.installAgent)
        
        #remove agent
        button = QtGui.QPushButton("Remove agent")
        self.mainLayout.addWidget(button)
        self.connect(button, QtCore.SIGNAL("clicked()"), self.removeAgent)
        
        # Create package
        button = QtGui.QPushButton("Create package")
        self.mainLayout.addWidget(button)
        self.connect(button, QtCore.SIGNAL("clicked()"), self.createPackage)
        
    def installAgent(self):
        self.emit(QtCore.SIGNAL("installAgent"))
            
    def removeAgent(self):
        self.emit(QtCore.SIGNAL("removeAgent"))
        
    def startAllNodes(self):
        self.emit(QtCore.SIGNAL("startAllNodes"))
        
    def stopAllNodes(self):
        self.emit(QtCore.SIGNAL("stopAllNodes"))
        
    def createPackage(self):
        self.emit(QtCore.SIGNAL("createPackage"))
        
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
