'''
Created on Sep 23, 2009

@author: juanmarcus
'''

class Task(object):
    def __init__(self, cmd, pars):
        self.cmd = cmd
        self.pars = pars
        self.issyscmd = False
        self.output = None
        
    def getCommandLine(self):
        return "lol"
    
    def setSystemCommand(self, bool):
        self.issyscmd = bool
        
    def makeCommand(self):
        parts = []
        #make main command
        if not self.issyscmd:
            cmd = "./" + self.cmd
        else:
            cmd = self.cmd    
        parts.append(cmd)
        
        #make parameters
        if self.pars:
            parts.append(self.pars)
        
        return " ".join(parts)

    def setOutput(self, output):
        self.output = output
        
    def getOutput(self):
        return self.output