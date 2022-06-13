class Loan(object):

    def __init__(self):
        self.id = None
        self.bankId = None
        self.borrowerId = None
        self.principle = None
        self.noOfYears = None
        self.interestRate = None

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

    def setPrinciple(self,principle):
        self.principle = principle

    def getPrinciple(self):
        return self.principle

    def setNoOfYears(self,noOfYears):
        self.noOfYears = noOfYears

    def getNoOfYears(self):
        return self.noOfYears
    
    def setInterestRate(self,interestRate):
        self.interestRate = interestRate

    def getInterestRate(self):
        return self.interestRate

