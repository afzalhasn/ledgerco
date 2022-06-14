class PaymentController(object):

    def __init__(self, paymentService):
        self.paymentService = paymentService

    def addPayment(self,id,bankId,borrowerId,lumpSumAmount,emiNo):
        return self.paymentService.addPayment(id,bankId,borrowerId,lumpSumAmount,emiNo)

    def getPaymentDetails(self,bankName,borrowerName):
        payment_details = []
        for paymentId in self.paymentService.paymentDetails:
            payment_detail = {}
            payment = self.paymentService.paymentDetails.get(paymentId)
            if payment.getBankName() == bankName and payment.getBorrowerName() == borrowerName:
                lumpSumAmount = payment.getLumpSumAmount()
                emiNo = payment.getEmiNo()
                payment_detail = {
                    'emi_no' : emiNo,
                    'lumpSumAmount': lumpSumAmount
                }
                payment_details.append(payment_detail)
        return payment_details
