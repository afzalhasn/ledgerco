import abc

class BalanceServiceInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def addBalance(self,id,bankId,borrowerId,emiNo):
        pass

