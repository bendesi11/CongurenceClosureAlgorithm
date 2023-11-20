from equvalenceClass import Equivalence
class EquivalenceClasses:
    def __init__(self,listOfEquvalence):
        self.listOfEquvalence = listOfEquvalence
    
    def __repr__(self):
        for equvalence in self.listOfEquvalence:
            listOfVer = equvalence.getAllElem()
            res = f"{listOfVer[0].parent}: [" 
            for ver in listOfVer:
                res = res + f"{ver.verticle},"
            res = res + "]"
            res = res + "\n"
        return res


    def find(self,verticle):
        for equivalence in self.listOfEquvalence:
            if verticle in equivalence.getAllElem():
                return equivalence.parent
            if any(verticle.name == currentVerticle.verticle for currentVerticle in equivalence.getAllElem()):
                return equivalence.parent
        return None
    
    def list(self, equvalence):
        if equvalence is None:
            return []
        return equvalence.getAllElem()
    
    def union(self, fristEquvalence, secoundEqucalence):
        
        if secoundEqucalence in self.listOfEquvalence:
            fristEquvalence.children.append(secoundEqucalence)
            self.listOfEquvalence.remove(secoundEqucalence)