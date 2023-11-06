import unittest
from graphClass import Graph

class MyClass:
    def __init__(self, value):
        self._data = value

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, new_value):
        if new_value != self._data:
            print(f"Adattag értéke megváltozott: {self._data} -> {new_value}")
            self._data = new_value




class unitTeszt(unittest.TestCase):
    def assertGraphEqual(self, res, expecterRes, parents = None):
        if parents is None:
            parents = []
        if res.name != expecterRes.name:
            raise AssertionError(f"({res.name}) nem egyezik meg a várt ({expecterRes.value}) eredménnyel")
        if res.value != expecterRes.value:
            raise AssertionError(f"({res.value}) nem egyezik meg a várt ({expecterRes.value}) eredménnyel")
        if hasattr(res, "children") != hasattr(expecterRes,"children"):
            raise AssertionError("Nem egyeznek a gyermekek száma!")
        if hasattr(res,"children"):
            if len(res.children) != len(expecterRes.children):
                raise AssertionError("Nem egyeznek a gyermekek száma!")
            for i in range(len(res.children)):
                if res in parents:
                    return
                parents.append(res)
                self.assertGraphEqual(res.children[i],expecterRes.children[i],parents.copy())

    def test_Graph(self):
        elsograf = Graph("elso","1")
        self.assertGraphEqual(elsograf,Graph("elso","1"))

    def test_Complex_Graph(self):
        elsograf = Graph("elso","1")
        masodik = Graph("masodik","2",[elsograf])
        harmadik = Graph("harmadik","3")
        negyed = Graph("negyed","4",[elsograf,masodik,harmadik])
        self.assertGraphEqual(negyed, Graph("negyed", "4", [Graph("elso", "1"), Graph("masodik", "2", [Graph("elso", "1")]), Graph("harmadik", "3")]))

    def test_not_Equal(self):
        self.assertGraphEqual(Graph("elso","2"),Graph("elso","1"))
    
    #def circle_Graph(self):
        #TODO
if __name__ == '__main__':
    unittest.main()