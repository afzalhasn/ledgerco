import abc

class PaymentServiceInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def addPayment(self,id,bankId,borrowerId,lumpSumAmount,emiNo):
        pass

