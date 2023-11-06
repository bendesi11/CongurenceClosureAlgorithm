class Signature:
    def __init__(self):
        self.signatureTable = []
    
    def enter(self, signature):
        self.signatureTable.append(signature)
    
    def enterVerticle(self, verticle):
        self.signatureTable.append([verticle, verticle.children])

    def delete(self, signature):
        self.signatureTable.remove(signature)
    
    def deleteVerticle(self,verticle):
        for signature in self.signatureTable:
            if signature[0] == verticle:
                self.signatureTable.remove(signature)

    #currentSignature searched signature
    #signature one of signatureTable elements
    def compare(self, currentSignature,signature):
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

    #graph: searched graph
    #signatureTable[0] = signature name/verticle
    #signatureTable[1] = list of signature elements
    def query(self, verticle):
        sameSignature = False
        currentSignature = verticle.children
        for signature in self.signatureTable:
            if self.compare(currentSignature, signature[1]):
                if verticle == signature[0]:
                    continue
                sameSignature = True
                return signature[0]#the namespace 
        return sameSignature
    
    def querySignature(self, currentSignature):
        sameSignature = False
        for signature in self.signatureTable:
            if self.compare(currentSignature[1], signature[1]):
                if currentSignature[0] == signature[0]:
                    continue
                sameSignature = True
                return signature[0]#the namespace 
        return sameSignature
