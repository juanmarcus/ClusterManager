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
    
    file1 = api.addFile(path="data/file1.txt")
    file2 = api.addFile(path="data/file2.txt", autoRemove = False)
    output = api.addFile(path="data/output.txt", autoSend=False, autoFetch=True)
    
    #create job
    job1 = api.createJob("Accumulate and Detect")
    
    #add commands
#    job1.addTask('accumulate_ga2h_point_line_naive', '-bounds 2 -90 90 -90 90 -delta 1 -inputdata "id220834478_input_data.dat" -outputmap "id220834478_job1_resulting_map.dat" >> id220834478_job1.log')
#    job1.addTask('echo',"' ' >> id220834478_job1.log")#.setSystemCommand(True)
#    job1.addTask('detect_peaks_ga2h_line','-inputmap "id220834478_job1_resulting_map.dat" -filter_size 5 -filter_std 0.5 -outputblades "id220834478_job1_resulting_blades.dat"')#  >> id220834478_job1.log')
    job1.addTask('cat', 'file1.txt > output.txt').setSystemCommand(True)
    job1.addTask('cat','file2.txt >> output.txt').setSystemCommand(True)
    job1.addTask('cat', 'file1.txt').setSystemCommand(True)
    
    #associate files
    job1.addFile(file1)
    job1.addFile(file2)
    job1.addFile(output)
    
    #start all clients
    api.startAllClients()
    
    #run all jobs
    api.runAllJobs()
