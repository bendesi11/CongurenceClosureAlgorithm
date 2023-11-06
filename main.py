from graphClass import Graph
from equvalenceClass import Equivalence
from quvalenceClasses import EquivalenceClasses
from signatureClass import Signature
def main():
    #graph test
    elsograf = Graph("elso","1")
    masodik=Graph("masodik","2",[elsograf])
    harmadik=Graph("harmadik","3")
    negyed=Graph("negyed","4",[elsograf,masodik,harmadik])
    elsograf.children=[negyed,harmadik]
    negyed.printGraph()


    hat = Graph("hat","6")
    het=Graph("het","7",[hat])
    nyolc=Graph("nyolc","8")
    kilenc=Graph("kilenc","9",[hat,het,nyolc])

    #congurence test
    maincongurence = Equivalence(elsograf,[harmadik])
    maincongurence.printEquivalence()
    maincongurence.append(masodik)
    maincongurence.children[0].append(negyed)
    maincongurence.children[1].append(negyed)
    maincongurence.printEquivalence()
    parents = maincongurence.getAllElem()
    secoundEquivalence = Equivalence(hat)
    secoundEquivalence.append(het)
    secoundEquivalence.append(nyolc)
    secoundEquivalence.children[0].append(kilenc)
    classes = EquivalenceClasses([maincongurence,secoundEquivalence])
    print(classes.find(het))
    print(classes.find(nyolc))
    print(classes.find(masodik))
    print(classes.list(maincongurence))
    print(classes.list(secoundEquivalence))
    classes.union(maincongurence,secoundEquivalence)
    print(classes.find(het))
    print(classes.find(nyolc))
    print(classes.find(masodik))
    print(classes.list(maincongurence))
    print(classes.list(secoundEquivalence))

    signatureTable = Signature()
    signatureTable.enterVerticle(maincongurence)
    signatureTable.enterVerticle(secoundEquivalence)
    signatureTable.enterVerticle(Equivalence(elsograf,[harmadik]))
    signatureTable.enterVerticle(Equivalence(masodik,[harmadik]))
    signatureTable.enter([negyed,[harmadik]])
    print(signatureTable.query(Equivalence(nyolc,[harmadik])))
    print(signatureTable.query(maincongurence))
    print(signatureTable.querySignature([hat,[harmadik]]))

    signatureTable.deleteVerticle(maincongurence)


    


    input("Press Enter to continue...")


if __name__ == "__main__":
    main()