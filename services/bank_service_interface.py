import abc

class BankServiceInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def addBank(self,id,name):
        pass

