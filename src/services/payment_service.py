from src.services.payment_service_interface import PaymentServiceInterface 
from src.models.payment import Payment

class PaymentService(PaymentServiceInterface):

    paymentDetails = {}

    def addPayment(self,id,bankName,borrowerName,lumpSumAmount,emiNo):
        payment = Payment()
        payment.setId(id)
        payment.setBankName(bankName)
        payment.setBorrowerName(borrowerName)
        payment.setLumpSumAmount(lumpSumAmount)
        payment.setEmiNo(emiNo)
        self.__class__.paymentDetails[id] = payment
        return payment

