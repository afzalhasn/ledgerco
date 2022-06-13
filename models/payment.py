class Payment(object):

    def __init__(self):
        self.id = None
        self.bankId = None
        self.borrowerId = None
        self.lumpSumAmount = None
        self.emiNo = None

    def setId(self,id):
        self.id = id

    def getId(self):
        return self.id

    def setBankId(self,bankId):
        self.bankId = bankId

    def getBankId(self):
        return self.bankId

    def setBorrowerId(self,borrowerId):
        self.borrowerId = borrowerId

    def getBorrowerId(self):
        return self.borrowerId

    def setLumpSumAmount(self,lumpSumAmount):
        self.lumpSumAmount = lumpSumAmount

    def getLumpSumAmount(self):
        return self.lumpSumAmount

    def setEmiNo(self,emiNo):
        self.emiNo = emiNo

    def getEmiNo(self):
        return self.emiNo

