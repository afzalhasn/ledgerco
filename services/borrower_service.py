from ledgerco.services.borrower_service_interface import BorrowerServiceInterface 
from ledgerco.models.borrower import Borrower 

class BorrowerService(BorrowerServiceInterface):

    borrowerDetails = {}

    def addBorrower(self,id,name):
        borrower = Borrower()
        borrower.setId(id)
        borrower.setName(name)
        self.__class__.borrowerDetails[id] = borrower
        return borrower

