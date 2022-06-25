from src.controllers.bank_controller import BankController 
from src.controllers.borrower_controller import BorrowerController 
from src.controllers.balance_controller import BalanceController 
from src.controllers.loan_controller import LoanController 
from src.controllers.payment_controller import PaymentController 

from src.services.bank_service import BankService 
from src.services.borrower_service import BorrowerService 
from src.services.balance_service import BalanceService 
from src.services.loan_service import LoanService 
from src.services.payment_service import PaymentService 

bankController     = BankController(BankService())
borrowerController = BorrowerController(BorrowerService())
balanceController  = BalanceController(BalanceService())
loanController     = LoanController(LoanService())
paymentController  = PaymentController(PaymentService())

class Driver(object):
    def __init__(self):
        self.balance_id = 0
        self.loan_id = 0
        self.payment_id = 0

    def applyLoan(self, input_data):
        self.loan_id += 1
        bank_name = input_data[1]
        borrower_name = input_data[2]
        principle_amount = int(input_data[3])
        no_of_years = int(input_data[4])
        rate_interest = int(input_data[5])
        bankController.addBank(f'bank{self.loan_id}',bank_name)
        borrowerController.addBorrower(f'borrower{self.loan_id}',borrower_name)
        loanController.addLoan(f'loan{self.loan_id}',bank_name,borrower_name,principle_amount,no_of_years,rate_interest)

    def applyPayment(self, input_data):
        self.payment_id += 1
        bank_name = input_data[1]
        borrower_name = input_data[2]
        lumpsum_amount = int(input_data[3])
        emi_no = int(input_data[4])
        paymentController.addPayment(f'payment{self.payment_id}',bank_name,borrower_name,lumpsum_amount,emi_no)

    def applyBalance(self, input_data):
        self.balance_id += 1
        bank_name = input_data[1]
        borrower_name = input_data[2]
        emi_no = int(input_data[3])
        balanceController.addBalance(f'balance{self.balance_id}',bank_name,borrower_name,emi_no)
        loan_details = loanController.getLoanDetails(bank_name, borrower_name)
        payment_details = paymentController.getPaymentDetails(bank_name, borrower_name)
        result = balanceController.getBalance(f'balance{self.balance_id}',loan_details, payment_details)
        return result

def startApp(Lines):
    obj = Driver()
    final_result = []
    for line in Lines:
        input_data = line.split()
        if input_data[0].upper() == 'LOAN':
            obj.applyLoan(input_data)
        elif input_data[0].upper() == 'PAYMENT':
            obj.applyPayment(input_data)
        elif input_data[0].upper() == 'BALANCE':
            result = obj.applyBalance(input_data)
            final_result.append(result)
    return final_result
