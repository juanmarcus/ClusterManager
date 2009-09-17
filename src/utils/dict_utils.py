'''
Created on Sep 16, 2009

@author: juanmarcus
'''

def safeGetValue(args, name, default = None):
    try:
        return args[name]
    except KeyError:
        return default