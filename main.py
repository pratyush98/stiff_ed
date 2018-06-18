import numpy as np
import nodes as nd
import pandas as pd
import ploting as pt
import stiffness as stf
import stiffness_truss as stf_t
import forces_gen as frc
nodes={}
inputw=raw_input("do you want to add a node.. ")
ctr=0
while inputw=="yes":
    (inputx,inputy,inputproperty,force_x,force_y)=raw_input("(xcoordinate,ycoordinate,property,force_x,force_y) ")[1:-1].split(",")
    ctr+=1
    nodes[str(ctr)]=nd.nodes(inputx,inputy,ctr,inputproperty,force_x,force_y)
    inputw=raw_input("do you want to add a node.. ")
#inputting connections..
for i in nodes:
    connections=raw_input("input the connections for "+str(i)+" ").split(",")
    connection=[nodes[j] for j in connections]
    nodes[i].linking(connection)
dict_c={"fixed":"r","unfixed":"b"}
#colors=[dict_c[i.property] for i in nodes]
pt.plote(nodes)
freedom_degree=stf.freedom(nodes)
print freedom_degree
inds=np.hstack([[str(i.x)+" "+str(i.number)+"x" for i in nodes.values()],[str(i.y)+" "+str(i.number)+"y" for i in nodes.values()]])
esm=pd.DataFrame(columns=inds,index=inds,data=0.0)
stiff_mat=stf_t.elementstiffness(nodes,esm)
print(stiff_mat)
force_vals=frc.get_forces(stiff_mat,nodes)
print force_vals