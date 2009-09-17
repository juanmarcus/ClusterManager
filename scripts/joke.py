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
    api.addFile("file1.txt", path = "data/file1.txt")
    api.addFile("outfile.txt", existing = False)
    
    #create jobs
    job1 = Job("cat {file1.txt} > {outfile.txt}")
    api.addJob(job1)
    
    #start all clients
    api.startAllClients()
    
    #run all jobs
    api.runAllJobs()