from graphClass import Graph

class ObservableList(list):
    def __init__(self):
        return

    def append(self, item):
        super(ObservableList, self).append(item)

class Equivalence:
    def __init__(self, verticle, childrens = None):
        self.verticle = verticle.name
        self.value = verticle.value
        self.parent = self
        self.children = ObservableList()
        if childrens is not None:
            equivalenceList = ObservableList()
            for children in childrens:
                equivalenceElem = Equivalence(children)
                equivalenceElem.parent = self.parent
                equivalenceList.append(equivalenceElem)
            self.children = equivalenceList
    def __repr__(self):
        return f'Name: {self.verticle}'
    
    def setParent(self, newParent, parents = None):
        if parents is None:
            parents = []
        parents.append(self)
        self.parent = newParent
        for children in self.children:
            if any(verticle.verticle == children.verticle for verticle in parents):
                continue
            children.setParent(newParent, parents)
    
    def append(self, item):
        if isinstance(item, Equivalence):
            item.setParent(self.parent)
            self.children.append(item)
        else:
            equivalence = Equivalence(item)
            equivalence.parent = self.parent
            self.children.append(equivalence)
    
  
    def getAllElem(self, parents = None):
        if parents is None:
            parents = []
        parents.append(self)
        if len(self.children) > 0:
            for children in self.children:
                if any(verticle.verticle == children.verticle for verticle in parents):
                    continue
                children.getAllElem(parents)
        return parents




    def printEquivalence(self,childrenCount = 0,parents = None):
        if parents is None:
            parents = []
        if childrenCount == 0:
            print("A ekvivalenciád felépítése: ")
        print(self.verticle + "(" + self.value + ")")
        if self in parents:
            print("Kör van a gráfban!")
            print("")
            return 1
        parents.append(self)
        round = 0
        if len(self.children) > 0:
            for children in self.children:
                print("-"*childrenCount + "-> ", end = "")
                round = children.printEquivalence(childrenCount+1,parents.copy())
                if round == 1:
                    continue
        print("")
        return 0