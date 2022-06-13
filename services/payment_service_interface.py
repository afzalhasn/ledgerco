import abc

class PaymentServiceInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def addPayment(self,id,bankName,borrowerName,lumpSumAmount,emiNo):
        pass

