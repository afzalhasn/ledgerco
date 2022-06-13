import math
from ledgerco.controllers.loan_controller import LoanController
from ledgerco.controllers.payment_controller import PaymentController

class BalanceController(object):

    def __init__(self, balanceService):
        self.balanceService = balanceService

    def addBalance(self,id,bankName,borrowerName,emiNo):
        return self.balanceService.addBalance(id,bankName,borrowerName,emiNo)

    def getBalance(self,Id,loan_details,payment_details):
        lumpsum_amount = 0
        total_paid = 0
        balance = self.balanceService.balanceDetails.get(Id)
        emi_amount = loan_details['emi_rate'] * balance.getEmiNo()
        total_amount = loan_details['total_amount']
        for payment in payment_details:
            if balance.getEmiNo() >= payment['emi_no']:
                lumpsum_amount += payment['lumpSumAmount']
        total_paid = emi_amount + lumpsum_amount
        remaining_emi = math.ceil((total_amount - total_paid ) / loan_details['emi_rate'])
        return [balance.getBankName(), balance.getBorrowerName(), total_paid, remaining_emi]
