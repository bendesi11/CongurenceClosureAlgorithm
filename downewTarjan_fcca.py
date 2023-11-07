from graphClass import *
from equvalenceClass import Equivalence
from quvalenceClasses import EquivalenceClasses
from signatureClass import Signature

#downey_tarjan fcca -fast concurrence closure algorithm 
def fccaDowneyTarjan(graph,equivalenceclasses,signatureTable):
    pending = getVerticlesWithChildren(graph)
    while pending != None:
        combine = []
        for v in pending:
            query_response = signatureTable.query(v)
            if type(query_response == bool):
                signatureTable.enterVerticle(v)
            else:
                combine.append([v, query_response])
        pending = []
        for combine_verticles in combine:
            if(equivalenceclasses.find(combine_verticles[0]) != equivalenceclasses.find(combine_verticles[0])):
                if(len(list(combine_verticles[0],signatureTable)) < len(list(combine_verticles[1],signatureTable))):
                    for u in list(combine_verticles[0],signatureTable):
                        signatureTable.remove(u)
                        pending.append(u)
                    #union()


def fccaDowneyTarjan_init(graph, equivalencerelations):
    equivalenceclasses = EquivalenceClasses([])
    for equivalencerelationElem in equivalencerelations:
        if equivalenceclasses.find(equivalencerelationElem[0]) is not None:
            equivalenceclasses.find(equivalencerelationElem[0]).append(equivalencerelationElem[1])
        if equivalenceclasses.find(equivalencerelationElem[1]) is not None:
            equivalenceclasses.find(equivalencerelationElem[1]).append(equivalencerelationElem[0])
        if equivalenceclasses.find(equivalencerelationElem[0]) is None and equivalenceclasses.find(equivalencerelationElem[1]) is None:
            equivalenceclasses.listOfEquvalence.append(Equivalence(equivalencerelationElem[0],equivalencerelationElem[1]))
    signatureTable = Signature()
    return fccaDowneyTarjan(graph,equivalenceclasses,signatureTable)

