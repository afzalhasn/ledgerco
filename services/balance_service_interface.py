import abc

class BalanceServiceInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def addBalance(self,id,bankName,borrowerName,emiNo):
        pass

