# Append parent directory to avoid import error
import sys
sys.path.append('../')
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

balance_id = 0
loan_id = 0
payment_id = 0

data_list = [
    "LOAN IDIDI Dale 5000 1 6",
    "LOAN MBI Harry 10000 3 7",
    "LOAN UON Shelly 15000 2 9",
    "PAYMENT IDIDI Dale 1000 5",
    "PAYMENT MBI Harry 5000 10",
    "PAYMENT UON Shelly 7000 12",
    "BALANCE IDIDI Dale 3",
    "BALANCE IDIDI Dale 6",
    "BALANCE UON Shelly 12",
    "BALANCE MBI Harry 12",
]

for data in data_list:
    input_data = data.split()
    if input_data[0].upper() == 'LOAN':
        bank_name = input_data[1]
        borrower_name = input_data[2]
        principle_amount = int(input_data[3])
        no_of_years = int(input_data[4])
        rate_interest = int(input_data[5])
        loan_id += 1
        bankController.addBank(f'bank{loan_id}',bank_name)
        borrowerController.addBorrower(f'borrower{loan_id}',borrower_name)
        loanController.addLoan(f'loan{loan_id}',bank_name,borrower_name,principle_amount,no_of_years,rate_interest)
    elif input_data[0].upper() == 'PAYMENT':
        payment_id += 1
        bank_name = input_data[1]
        borrower_name = input_data[2]
        lumpsum_amount = int(input_data[3])
        emi_no = int(input_data[4])
        paymentController.addPayment(f'payment{payment_id}',bank_name,borrower_name,lumpsum_amount,emi_no)
    elif input_data[0].upper() == 'BALANCE':
        balance_id += 1
        bank_name = input_data[1]
        borrower_name = input_data[2]
        emi_no = int(input_data[3])
        balanceController.addBalance(f'balance{balance_id}',bank_name,borrower_name,emi_no)
        loan_details = loanController.getLoanDetails(bank_name, borrower_name)
        payment_details = paymentController.getPaymentDetails(bank_name, borrower_name)
        result = balanceController.getBalance(f'balance{balance_id}',loan_details, payment_details)
        print(*result)

