import math

class LoanController(object):

    def __init__(self, loanService):
        self.loanService = loanService

    def addLoan(self,id,bankName,borrowerName,principle,noOfYears,interestRate):
        return self.loanService.addLoan(id,bankName,borrowerName,principle,noOfYears,interestRate)

    def getEmiCount(self, loanId):
        loan = self.loanService.loanDetails.get(loanId)
        return loan.noOfYears * 12

    def getLoanAmount(self, loanId):
        loan = self.loanService.loanDetails.get(loanId)
        self.p = loan.principle
        self.n = loan.noOfYears
        self.r = loan.interestRate
        return math.ceil(self.p*self.n*self.r*0.01 + self.p)

    def getEmiRate(self, loanId):
        loan_amount = self.getLoanAmount(loanId)
        return math.ceil(loan_amount / (self.n*12) )

    def getLoanDetails(self,bankName,borrowerName):
        loan_details = {}
        for loanId in self.loanService.loanDetails:
            loan =  self.loanService.loanDetails.get(loanId)
            if loan.getBankName() == bankName and loan.getBorrowerName() == borrowerName:
                emi_rate = self.getEmiRate(loanId)
                emi_count = self.getEmiCount(loanId)
                loan_details['emi_rate'] = emi_rate
                loan_details['emi_count'] = emi_count
                loan_details['total_amount'] = self.getLoanAmount(loanId)
                break
        return loan_details
