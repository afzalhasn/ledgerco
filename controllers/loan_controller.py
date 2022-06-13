import math

class LoanController(object):

    def __init__(self, loanService):
        self.loanService = loanService

    def addLoan(self,id,bankId,borrowerId,principle,noOfYears,interestRate):
        return self.loanService.addLoan(id,bankId,borrowerId,principle,noOfYears,interestRate)

    def getEmiRate(self, loanId):
        loan_details = self.loanService.loanDetails.get(loanId)
        p = loan_details.principle
        n = loan_details.noOfYears
        r = loan_details.interestRate
        return math.ceil((p*n*r*0.01 + p)/(n*12)), n*12
