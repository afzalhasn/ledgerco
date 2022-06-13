import abc

class LoanServiceInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def addLoan(self,id,bankId,borrowerId,principle,noOfYears,interestRate):
        pass

