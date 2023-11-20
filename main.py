from graphClass import Graph
from equvalenceClass import Equivalence
from quvalenceClasses import EquivalenceClasses
from signatureClass import Signature
from downewTarjan_fcca import fccaDowneyTarjan_init
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

    alma = classes.find(het)
    print(type(alma))

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

    chatGPT = Graph("A","1",[Graph("B","1",[Graph("D","1",[Graph("C","1")])])])
    chatGPT.children.append(chatGPT.children[0].children[0].children[0])
    chatGPT.children[0].children.append(chatGPT)
    chatGPT.children[0].children[0].children.append(chatGPT.children[0])
    chatGPT.children[0].children[0].children[0].children = [chatGPT]
    chatGPT.children[0].children[0].children[0].children.append(chatGPT.children[0].children[0])

    
    chatGPT.printGraph()
    ceg1Congurence = Equivalence(chatGPT,[chatGPT.children[0]])
    ceg2Congurence = Equivalence(chatGPT.children[0].children[0],[chatGPT.children[0].children[0].children[0]])
    cegek = EquivalenceClasses([ceg1Congurence,ceg2Congurence])

    cegek=[[chatGPT,chatGPT.children[0]],[chatGPT.children[0].children[0],chatGPT.children[0].children[0].children[0]]]

    chatGPTD = Graph("D","1")
    chatGPTA = Graph("A","1")
    chatGPTB = Graph("B","1")
    chatGPTC = Graph("C","1")
    chatGPTE = Graph("E","1")
    chatGPTD.children = [chatGPTA]
    chatGPTA.children = [chatGPTD,chatGPTB]
    chatGPTB.children = [chatGPTA,chatGPTC]
    chatGPTC.children = [chatGPTB,chatGPTE]
    chatGPTE.children = [chatGPTC]
    cegek=[[chatGPTA,chatGPTB],[chatGPTC,chatGPTE]]

    fccaDowneyTarjan_init(chatGPT,cegek)

    input("Press Enter to continue...")


if __name__ == "__main__":
    main()