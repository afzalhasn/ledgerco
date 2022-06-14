from src.services.bank_service_interface import BankServiceInterface 
from src.models.bank import Bank 

class BankService(BankServiceInterface):

    bankDetails = {}

    def addBank(self,id,name):
        bank = Bank()
        bank.setId(id)
        bank.setName(name)
        self.__class__.bankDetails[id] = bank
        return bank
