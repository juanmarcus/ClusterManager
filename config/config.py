#required function config receives a ConfigProxy object
#you can't set a node password here yet. Use dsa keys for auto login
def config(api):
    #hosts
    node = api.addNode("illidan")
#    node.setUserName("athena")
    node.setWorkingDir("/home/juanmarcus/tmp")
    node.setWorkload(2)
    #node.setDisplay("0")
    
    
