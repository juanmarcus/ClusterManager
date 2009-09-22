import sys

class Callback(object):
    def error(self, msg):
        print msg
        sys.exit(0)

def run(api):
    #set callback object
    api.setCallback(Callback())
    
    # Define files to manage.
    #
    # The name of the file should be used in the commands without the path.
    #
    # required options:
    #    path - local file
    #
    # default options:
    #    autoSend = True
    #    autoFetch = False
    #    autoRemove = True
    
    inputdata = api.addFile(path="data/id220834478_input_data.dat")
    resultingmap = api.addFile(path="data/id220834478_job1_resulting_map.dat", autoSend=False, autoFetch=True)
    outputblades = api.addFile(path="data/id220834478_job1_resulting_blades.dat", autoSend=False, autoFetch=True)
    logfile = api.addFile(path="data/id220834478_job1.log", autoSend=False, autoFetch=True)
    
    #create job
    job1 = api.createJob("Accumulate and Detect")
    
    #add commands
    job1.addCommand('/home/athena/laffernandes/accumulate_ga2h_point_line_naive -bounds 2 -90 90 -90 90 -delta 1 -inputdata "id220834478_input_data.dat" -outputmap "id220834478_job1_resulting_map.dat" >> id220834478_job1.log')
    job1.addCommand("echo ' ' >> id220834478_job1.log")
    job1.addCommand('/home/athena/laffernandes/detect_peaks_ga2h_line -inputmap "id220834478_job1_resulting_map.dat" -filter_size 5 -filter_std 0.5 -outputblades "id220834478_job1_resulting_blades.dat"  >> id220834478_job1.log')
    
    #associate files
    job1.addFile(inputdata)
    job1.addFile(resultingmap)
    job1.addFile(outputblades)
    job1.addFile(logfile)
    
    #start all clients
    api.startAllClients()
    
    #run all jobs
    api.runAllJobs()
