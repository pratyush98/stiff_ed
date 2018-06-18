import numpy as np
from numpy.linalg import inv
import pandas as pd
def get_forces(stiff_mat,nodes):
    forces={}
    disp={}
    arrw=[]
    arrc=[]
    indf=[]
    for i in nodes.values():
        forces[str(i.x)+" "+str(i.number)+"x"]=i.forcex
        forces[str(i.y)+" "+str(i.number)+"y"]=i.forcey
        if i.property!="fixed":
            arrc.append(i.forcex)
            indf.append(str(i.x)+" "+str(i.number)+"x")
            disp[str(i.x)+" "+str(i.number)+"x"]=-1
            arrc.append(i.forcey)
            indf.append(str(i.y)+" "+str(i.number)+"y")
            disp[str(i.y)+" "+str(i.number)+"y"]=-1
        if i.property=="fixed":
            disp[str(i.x)+" "+str(i.number)+"x"]=0
            disp[str(i.y)+" "+str(i.number)+"y"]=0
    for i in indf:
        arrw.append(stiff_mat.loc[i][indf])
    arrw=inv(arrw)
    disp1=np.sum(np.multiply(arrw,arrc),axis=1)
    ctr=0
    for i in indf:
        disp[i]=disp1[ctr]
        ctr+=1
    arrw=inv(stiff_mat.values)
    arrc=disp.values()
    force_x_y=np.sum(np.multiply(arrw,arrc),axis=1)
    return force_x_y
    
    