from ledgerco.services.balance_service_interface import BalanceServiceInterface 
from ledgerco.models.balance import Balance 

class BalanceService(BalanceServiceInterface):

    balanceDetails = {}

    def addBalance(self,id,bankId,borrowerId,emiNo):
        balance = Balance()
        balance.setId(id)
        balance.setBankId(bankId)
        balance.setBorrowerId(borrowerId)
        balance.setEmiNo(emiNo)
        self.__class__.balanceDetails[id] = balance
        return balance
