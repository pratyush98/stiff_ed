import matplotlib.pyplot as plt
def plote(nodes):
    x=[i.x for i in nodes.values()]
    y=[i.y for i in nodes.values()]
    conn=[]
    for i in nodes.values():
        for j in i.prevnodes:
            conn.append([[j.x,j.y],[i.x,i.y]])
    ax = plt.axes()
    ax.scatter(x,y,c='k', alpha=1, marker='s')
    for i in conn:
        plt.plot([i[0][0],i[1][0]],[i[0][1],i[1][1]], 'ro-')
    plt.show()
