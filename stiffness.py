def freedom(nodes):
    node_free={}
    for i in nodes.keys():
        if len(nodes[i].prevnodes)==1 and nodes[i].property=="fixed":
            node_free[i]=(0,0,0)
        elif len(nodes[i].prevnodes)==1 and nodes[i].property=="pivoted":
            node_free[i]=(0,0,1)
        elif len(nodes[i].prevnodes)>1:
            ctr=0
            for j in nodes[i].prevnodes:
                if len(j.prevnodes)==1:
                    ctr+=1
            if ctr>=2:
                node_free[i]=(0,0,1)
            elif ctr==1:
                node_free[i]=(1,0,1)
            else:
                node_free[i]=(1,1,1)
    return node_free