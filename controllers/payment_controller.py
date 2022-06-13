class PaymentController(object):

    def __init__(self, paymentService):
        self.paymentService = paymentService

    def addPayment(self,id,bankId,borrowerId,lumpSumAmount,emiNo):
        return self.paymentService.addPayment(id,bankId,borrowerId,lumpSumAmount,emiNo)
