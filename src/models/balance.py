class Balance(object):

    def __init__(self):
        self.id = None
        self.bankName = None
        self.borrowerName = None
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

    def setEmiNo(self,emiNo):
        self.emiNo = emiNo

    def getEmiNo(self):
        return self.emiNo

