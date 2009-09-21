from mothership.job.Job import Job
import sys

class Callback(object):
    def error(self, msg):
        print msg
        sys.exit(0)

def run(api):
    #set callback object
    api.setCallback(Callback())
    
    #define files to manage
    file1 = api.addFile("file1.txt", path = "data/file1.txt")
    file2 = api.addFile("outfile.txt", existing = False, fetch = True )
    
    #create job
    job1 = Job()
    
    #add commands
    job1.addCommand("cat file1.txt > outfile.txt")
    job1.addCommand("cat file1.txt >> outfile.txt")
    
    #associate files
    job1.addFile(file1)
    job1.addFile(file2)
    
    #register job
    api.addJob(job1)
    
    #start all clients
    api.startAllClients()
    
    #run all jobs
    api.runAllJobs()