class Loan(object):

    def __init__(self):
        self.id = None
        self.bankName = None
        self.borrowerName = None
        self.principle = None
        self.noOfYears = None
        self.interestRate = None

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

