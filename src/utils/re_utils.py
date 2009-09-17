'''
Created on Sep 16, 2009

@author: juanmarcus
'''
import re

def listTokens(cmd):
    return re.findall(r"\{([\w|\.]*)\}", cmd) 
