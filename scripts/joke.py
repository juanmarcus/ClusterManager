import sys

class Callback(object):
    def error(self, msg):
        print msg
        sys.exit(0)

def run(api):
    #set callback object
    api.setCallback(Callback())
    
    # Define files to manage
    #
    # required options:
    #    name
    #    path
    #
    # default options:
    #    autoSend = True
    #    autoFetch = False
    #    autoRemove = True
    
    file1 = api.addFile("file1.txt", path="data/file1.txt")
    file2 = api.addFile("file2.txt", path="data/file2.txt")
    outfile = api.addFile("outfile.txt", path="data/outfile.txt", autoSend = False, autoFetch=True)
    
    #create job
    job1 = api.createJob("Test job")
    
    #add commands
    job1.addCommand("cat file1.txt > outfile.txt")
    job1.addCommand("cat file2.txt >> outfile.txt")
    
    #associate files
    job1.addFile(file1)
    job1.addFile(file2)
    job1.addFile(outfile)
    
    #start all clients
    api.startAllClients()
    
    #run all jobs
    api.runAllJobs()
