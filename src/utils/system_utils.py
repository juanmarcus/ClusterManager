#run a system command and return the result
from subprocess import PIPE, Popen
def run_command(cmd):
    p = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
    out = " ".join(p.stdout.readlines())
    return out