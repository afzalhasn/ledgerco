import sys
sys.path.append('/Users/mhassa080/Documents/personal_proj/Data Structure and Algorithms/Project')
from ledgerco.controllers.bank_controller import BankController 
from ledgerco.controllers.borrower_controller import BorrowerController 
from ledgerco.controllers.balance_controller import BalanceController 
from ledgerco.controllers.loan_controller import LoanController 
from ledgerco.controllers.payment_controller import PaymentController 

from ledgerco.services.bank_service import BankService 
from ledgerco.services.borrower_service import BorrowerService 
from ledgerco.services.balance_service import BalanceService 
from ledgerco.services.loan_service import LoanService 
from ledgerco.services.payment_service import PaymentService 

bankController     = BankController(BankService())
borrowerController = BorrowerController(BorrowerService())
balanceController  = BalanceController(BalanceService())
loanController     = LoanController(LoanService())
paymentController  = PaymentController(PaymentService())

borrower1 = borrowerController.addBorrower('borrower1','Dale')
borrower2 = borrowerController.addBorrower('borrower2','Harry')
borrower3 = borrowerController.addBorrower('borrower3','Shelly')

bank1 = bankController.addBank('bank1','IDID')
bank2 = bankController.addBank('bank2','MBI')
bank3 = bankController.addBank('bank3','UON')

loan1 = loanController.addLoan('loan1','IDID','Dale',10000,5,4)
loan2 = loanController.addLoan('loan2','MBI','Harry',2000,2,2)
emi_rate, total_emi = (loanController.getEmiRate('loan1'))
print(loanController.getEmiRate('loan2'))
print(loanController.getEmiRate('loan1'))

balance1 = balanceController.addBalance('balance1','IDID','Dale',40)
print(balanceController.getUserBalance('balance1',emi_rate,total_emi))
# loan2 = loanController.addLoan('loan2','bank2','borrower2',2000,2,2)


# balance2 = balanceController.addBalance('balance1','bank1','borrower1',40)
