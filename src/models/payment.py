class Payment(object):

    def __init__(self):
        self.id = None
        self.bankName= None
        self.borrowerName= None
        self.lumpSumAmount = None
        self.emiNo = None

    def setId(self,id):
        self.id = id

    def getId(self):
        return self.id

    def setBankName(self,bankName):
        self.bankName = bankName

    def getBankName(self):
        return self.bankName

    def setBorrowerName(self,borrowerName):
        self.borrowerName = borrowerName

    def getBorrowerName(self):
        return self.borrowerName

    def setLumpSumAmount(self,lumpSumAmount):
        self.lumpSumAmount = lumpSumAmount

    def getLumpSumAmount(self):
        return self.lumpSumAmount

    def setEmiNo(self,emiNo):
        self.emiNo = emiNo

    def getEmiNo(self):
        return self.emiNo

