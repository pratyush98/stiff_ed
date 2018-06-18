import numpy as np
def matadd(theta,x1,y1,n1,x2,y2,n2,esm):
    mult=18/np.sqrt((y1-y2)**2+(x1-x2)**2)
    esm[str(x1)+" "+str(n1)+"x"][str(x1)+" "+str(n1)+"x"]+=np.cos(theta)**2*mult
    esm[str(y1)+" "+str(n1)+"y"][str(y1)+" "+str(n1)+"y"]+=np.sin(theta)**2*mult    
    esm[str(x2)+" "+str(n2)+"x"][str(x2)+" "+str(n2)+"x"]+=np.cos(theta)**2*mult    
    esm[str(y2)+" "+str(n2)+"y"][str(y2)+" "+str(n2)+"y"]+=np.sin(theta)**2*mult   
    esm[str(x1)+" "+str(n1)+"x"][str(y1)+" "+str(n1)+"y"]+=np.cos(theta)*np.sin(theta)*mult    
    esm[str(y1)+" "+str(n1)+"y"][str(x1)+" "+str(n1)+"x"]+=np.cos(theta)*np.sin(theta)*mult
    esm[str(x2)+" "+str(n2)+"x"][str(x1)+" "+str(n1)+"x"]+=-1*np.cos(theta)**2*mult   
    esm[str(x1)+" "+str(n1)+"x"][str(x2)+" "+str(n2)+"x"]+=-1*np.cos(theta)**2*mult 
    esm[str(y2)+" "+str(n2)+"y"][str(x1)+" "+str(n1)+"x"]+=-1*np.cos(theta)*np.cos(theta)*mult
    esm[str(x1)+" "+str(n1)+"x"][str(y2)+" "+str(n2)+"y"]+=-1*np.cos(theta)*np.cos(theta)*mult
    esm[str(y1)+" "+str(n1)+"y"][str(x2)+" "+str(n2)+"x"]+=-1*np.cos(theta)*np.cos(theta)*mult   
    esm[str(x2)+" "+str(n2)+"x"][str(y1)+" "+str(n1)+"y"]+=-1*np.cos(theta)*np.cos(theta)*mult
    esm[str(y1)+" "+str(n1)+"y"][str(y2)+" "+str(n2)+"y"]+=-1*np.sin(theta)**2*mult   
    esm[str(y2)+" "+str(n2)+"y"][str(y1)+" "+str(n1)+"y"]+=-1*np.sin(theta)**2*mult
    esm[str(x2)+" "+str(n2)+"x"][str(y2)+" "+str(n2)+"y"]+= np.cos(theta)*np.cos(theta)*mult   
    esm[str(y2)+" "+str(n2)+"y"][str(x2)+" "+str(n2)+"x"]+= np.cos(theta)*np.cos(theta)*mult
    return esm
def traverse(nodey,esm):
    for i in nodey.prevnodes:
        if i.visited==0:
            i.visited=1
            if (i.x-nodey.x)==0:
               theta=np.arctan(float(i.y-nodey.y)/(i.x-nodey.x))
            else:
               theta=np.pi/2
            matadd(theta,i.x,i.y,i.number,nodey.x,nodey.y,nodey.number,esm)
            esm=traverse(i,esm) 
    return esm
def elementstiffness(nodes,esm):
    start=nodes.keys()[0]
    nodes[start].visited=1
    esm=traverse(nodes[start],esm)
    for i in nodes.values():
        i.visited=0
    return esm