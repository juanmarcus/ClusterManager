#run a system command and return the result
from subprocess import PIPE, Popen

def run_command(cmd):
    '''
    Runs a system command and waits.
    
    @param cmd: The command to run
    
    Returns a tuple (returncode, stdout).
    '''
    p = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
    p.wait()
    returncode = p.returncode
    out = " ".join(p.stdout.readlines())
    return returncode, out
