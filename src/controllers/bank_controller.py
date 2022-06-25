class BankController(object):

    def __init__(self, bankService):
        self.bankService = bankService

    def addBank(self,id,name):
        return self.bankService.addBank(id,name)
