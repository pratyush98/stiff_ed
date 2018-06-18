class nodes:
    def __init__(self,x,y,no,property,forcex,forcey):
        self.x=int(x)
        self.y=int(y)
        self.property=property
        self.prevnodes=[]
        self.visited=0
        self.number=no
        self.forcex=int(forcex)
        self.forcey=int(forcey)
    def linking(self,nodey):
        self.prevnodes=nodey
    def details(self):
        print self.x
        print self.y
        print self.property
        print self.prevnode[0].x