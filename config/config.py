#required function config receives a ConfigProxy object
#you can't set a host password here yet. Use dsa keys for auto login
def config(api):
    #hosts
    host = api.addClient("illidan")
#    host.setUserName("athena")
    host.setWorkingDir("/home/juanmarcus/tmp")
    host.setWorkload(2)
    #host.setDisplay("0")
    
    
