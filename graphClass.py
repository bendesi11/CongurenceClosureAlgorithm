class Graph:
    def __init__(self,name, value, children = None):
        self.name = name
        self.value = value
        if children is not None:
            self.children = children
            
    def __repr__(self):
        return f'Name: {self.name}'

    #graf.printGraph
    def printGraph(self,childrenCount = 0,parents = None):
        if parents is None:
            parents = []
        if childrenCount == 0:
            print("A gráfod felépítése: ")#gyoker elem
        print(self.name + "(" + self.value + ")")
        if self in parents:
            print("Kör van a gráfban!")
            print("")
            return 1
        parents.append(self)
        round = 0
        if hasattr(self, "children"):
            for children in self.children:
                print("-"*childrenCount + "-> ", end = "")
                round = children.printGraph(childrenCount+1,parents.copy())
                if round == 1:
                    continue
        print("")
        return 0
        
    #binaris fava alakitsa a grafot
    def graphToBinaryGraph(self,parents = None):
        if parents is None:
            parents = []
        if self in parents:
            return Graph(self.name, self.value)
        parents.append(self)
        res = Graph(self.name, self.value)#create new graph
        if hasattr(self, 'children'):
            if(len(self.children) > 2):#more than 2 children
                resChildren = Graph("w("+self.name + ")", self.value)#create new graph for the origin vertice
                resChildren.children = self.children[1:]#set children without frist one
                res.children = [self.children[0].graphToBinaryGraph(parents.copy()), resChildren.graphToBinaryGraph(parents.copy())]#0 children->toBinary, new grap->toBinary
            elif(len(self.children) == 2):#only 2 children
                res.children = [self.children[0].graphToBinaryGraph(parents.copy()), self.children[1].graphToBinaryGraph(parents.copy())]
            else:#only one children, shouldnt need check because 31 line
                res.children = [self.children[0].graphToBinaryGraph(parents.copy())]
        return res#return binary graph
        
    #a graf csucsai (halmaz)listaban
    def verticles(self,parents = None):
        if parents is None:
            parents = []
        if self in parents:
            return parents#in list->stop
        parents.append(self)#add to the list
        if hasattr(self, "children"):
            for children in self.children:
                parents=children.verticles(parents)#overwrite the parent list with children list
        return parents


#ossze gyujti listaba a csucs gyerekeit(ez a graf signature-ja?)
def getSignature(graph):
    signatureTable = [graph,[]]
    if hasattr(graph,"children"):
        for children in graph.children:
            signatureTable[1].append(children)
    return signatureTable
    
    
#currentSignature keresendo signature
#signature a signatureTable-ben levo signature
def compare(currentSignature,signature):
    if len(currentSignature) != len(signature):
        return False
    for signatureElem in signature:
        if signatureElem not in currentSignature:
            return False
    return True

#graph: keresendo graf
#signatureTable: 2 elemu tomboket tarolo tomb
#signaturTable[0]=signature name
#signatureTable[1]=a signature elemei
def query(graph,signatureTable):
    sameSignature = False
    currentSignature = getSignature(graph)
    for signature in signatureTable:
        if compare(currentSignature[1], signature[1]):
            sameSignature = True
            return signature[0]#the namespace 
    return sameSignature
        
"""        
def getSignature(graph):
    signatureTable=[]
    signatureTable.append(graph.name)
    if hasattr(graph,"children"):
        for children in graph.children:
            grandsons=getSignature(children)
            for grandson in grandsons:
                if grandson not in signatureTable:
                    signatureTable.append(grandson)
    return signatureTable
    """
    
#graf gyerekeinek szama
def d(graph):
    if hasattr(graph,"children"):
        return len(graph.children)
    return 0

#return verticles where verticles.children>=1
def getVerticlesWithChildren(graph):
    verticles = graph.verticles()
    res = []
    for verticle in verticles:
        if d(verticle) >= 1:
            res.append(verticle)
    return res

#signature table[[egy,[ketto,harom],[ketto,[harom]]]]
def list(verticle, signatureTable):
    count = 0
    res=[]
    for signature in signatureTable:
        if verticle in signature[1]:
            count += 1
            res.append(signature)
    return res

def find(verticle, signatureTable):
    return query(verticle,signatureTable)

#downey_tarjan fcca -fast concurrence closure algorithm 
def fccaDowneyTarjan(graph):
    signatureTable = []
    pending = getVerticlesWithChildren(graph)
    while pending != None:
        combine = []
        for v in pending:
            query_response = query(v,  signatureTable)
            if type(query_response == bool):
                signature = getSignature(v)
                signatureTable.append(signature)
            else:
                combine.append([v,query_response])
        pending = []
        for combine_verticles in combine:
            if(combine_verticles[0].name != combine_verticles[1].name):
                if(len(list(combine_verticles[0],signatureTable)) < len(list(combine_verticles[1],signatureTable))):
                    for u in list(combine_verticles[0],signatureTable):
                        signatureTable.remove(u)
                        pending.append(u)
                    #union()
                    

def main():
    elsograf = Graph("elso","1")
    masodik=Graph("masodik","2",[elsograf])
    harmadik=Graph("harmadik","3")
    negyed=Graph("negyed","4",[elsograf,masodik,harmadik])
    elsograf.children=[negyed,harmadik]
    negyed.printGraph()


    print("masodik feladat vege")
    bin=negyed.graphToBinaryGraph()
    bin.printGraph()
    print(getSignature(negyed))
    print(d(negyed))
    print("query: ")
    print(query(harmadik,[getSignature(negyed)]))#query
    print(query(negyed,[getSignature(negyed)]))#query
    print(query(negyed,[]))#query
    print("list: ")
    print(list(negyed,[getSignature(negyed)]))
    print(list(harmadik,[getSignature(negyed)]))
    print(list(elsograf,[getSignature(negyed)]))

    #print(getVerticlesWithChildren(negyed))
    #if(harmadik):
    #    harmadik.printGraph()
    input("Press Enter to continue...")


if __name__ == "__main__":
    main()