class BalanceController(object):

    def __init__(self, balanceService):
        self.balanceService = balanceService

    def addBalance(self,id,bankId,borrowerId,emiNo):
        return self.balanceService.addBalance(id,bankId,borrowerId,emiNo)

    def getUserBalance(self,userId, emi_rate, total_emi):
        balance = self.balanceService.balanceDetails.get(userId)
        remaining_emi = total_emi - balance.getEmiNo()
        paid_balance = emi_rate*balance.getEmiNo()
        return (balance.getBankId(), balance.getBorrowerId(), paid_balance, remaining_emi)
