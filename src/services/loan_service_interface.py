import abc

class LoanServiceInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def addLoan(self,id,bankName,borrowerName,principle,noOfYears,interestRate):
        pass

