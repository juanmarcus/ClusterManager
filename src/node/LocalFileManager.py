'''
Created on Sep 28, 2009

@author: juanmarcus
'''

class LocalFileManager(object):
    def __init__(self):
        self.localfiles = []
    
    def addFile(self, filename):
        self.localfiles.append(filename)
        
    def hasFiles(self, files):
        '''
        Check if the client has a list of files.
         
        @param files: a list of filenames
        
        Return False if the client has not finished receiving at least one of the files.
        '''
        for file in files:
            if not file in self.localfiles:
                return False
        return True
