from graphClass import *
from equvalenceClass import Equivalence
from quvalenceClasses import EquivalenceClasses
from signatureClass import Signature

#downey_tarjan fcca -fast concurrence closure algorithm 
def fccaDowneyTarjan(graph,equivalenceclasses,signatureTable):
    pending = getVerticlesWithChildren(graph)
    while pending != []:
        combine = []
        for v in pending:
            query_response = signatureTable.query(v)
            if isinstance(query_response, bool):
                signatureTable.enterVerticle(v)
            else:
                combine.append([v, query_response])
        pending = []
        for combine_verticles in combine:
            if(equivalenceclasses.find(combine_verticles[0]) != equivalenceclasses.find(combine_verticles[1])):
                if(len(equivalenceclasses.list(equivalenceclasses.find(combine_verticles[0]))) < len(equivalenceclasses.list(equivalenceclasses.find(combine_verticles[1])))):
                    for u in equivalenceclasses.list(equivalenceclasses.find(combine_verticles[0])):
                        pending.append(u)
                    equivalenceclasses.union(equivalenceclasses.find(combine_verticles[1]),equivalenceclasses.find(combine_verticles[0]))

                else:
                    for u in equivalenceclasses.list(equivalenceclasses.find(combine_verticles[1])):
                        pending.append(u)
                    equivalenceclasses.union(equivalenceclasses.find(combine_verticles[0]),equivalenceclasses.find(combine_verticles[1]))
    print(equivalenceclasses)
    return equivalenceclasses


def fccaDowneyTarjan_init(graph, equivalencerelations):
    equivalenceclasses = EquivalenceClasses([])
    for equivalencerelationElem in equivalencerelations:
        if equivalenceclasses.find(equivalencerelationElem[0]) is not None:
            equivalenceclasses.find(equivalencerelationElem[0]).append([equivalencerelationElem[1]])
        if equivalenceclasses.find(equivalencerelationElem[1]) is not None:
            equivalenceclasses.find(equivalencerelationElem[1]).append([equivalencerelationElem[0]])
        if equivalenceclasses.find(equivalencerelationElem[0]) is None and equivalenceclasses.find(equivalencerelationElem[1]) is None:
            equivalenceclasses.listOfEquvalence.append(Equivalence(equivalencerelationElem[0],[equivalencerelationElem[1]]))
    signatureTable = Signature()
    return fccaDowneyTarjan(graph,equivalenceclasses,signatureTable)

