class Balance(object):

    def __init__(self):
        self.id = None
        self.bankId = None
        self.borrowerId = None
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

    def setEmiNo(self,emiNo):
        self.emiNo = emiNo

    def getEmiNo(self):
        return self.emiNo

