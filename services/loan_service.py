from ledgerco.services.loan_service_interface import LoanServiceInterface 
from ledgerco.models.loan import Loan 

class LoanService(LoanServiceInterface):

    loanDetails = {}

    def addLoan(self,id,bankName,borrowerName,principle,noOfYears,interestRate):
        loan = Loan()
        loan.setId(id)
        loan.setBankName(bankName)
        loan.setBorrowerName(borrowerName)
        loan.setPrinciple(principle)
        loan.setNoOfYears(noOfYears)
        loan.setInterestRate(interestRate)
        self.__class__.loanDetails[id] = loan
        return loan
