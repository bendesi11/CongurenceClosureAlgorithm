from equvalenceClass import Equivalence
class EquivalenceClasses:
    def __init__(self,listOfEquvalence):
        self.listOfEquvalence = listOfEquvalence
    
    def __repr__(self):
        res = ""
        for equivalence in self.listOfEquvalence:
            res += equivalence
        return res

    def find(self,verticle):
        for equivalence in self.listOfEquvalence:
            if verticle in equivalence.getAllElem():
                return equivalence.parent.verticle
            if any(verticle.name == currentVerticle.verticle for currentVerticle in equivalence.getAllElem()):
                return equivalence.parent.verticle
        return None
    
    def list(self, equvalence):
        return equvalence.getAllElem()
    
    def union(self, fristEquvalence, secoundEqucalence):
        fristEquvalence.append(secoundEqucalence)
        self.listOfEquvalence.remove(secoundEqucalence)
