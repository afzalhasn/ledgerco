from ledgerco.services.payment_service_interface import PaymentServiceInterface 
from ledgerco.models.payment import Payment

class PaymentService(PaymentServiceInterface):

    paymentDetails = {}

    def addPayment(self,id,bankId,borrowerId,lumpSumAmount,emiNo):
        payment = Payment()
        payment.setId(id)
        payment.setBankId(bankId)
        payment.setBorrowerId(borrowerId)
        payment.setLumpSumAmount(lumpSumAmount)
        payment.setEmiNo(emiNo)
        self.__class__.paymentDetails[id] = payment
        return payment
