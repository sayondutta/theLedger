from src.controller.controller import BaseController
from src.util.constants import PAYMENT_BANK_NOT_FOUND, PAYMENT_USER_NOT_FOUND, LOAN_NOT_TAKEN,ZERO_EMIS_LEFT
from src.dto.entities.payment import Payment


class PaymentController(BaseController):
    def __init__(self, storage):
        super().__init__(storage)

    def processRequest(self, request):
        bankID = self._storage.getBankID(request.bankName)
        if bankID is None:
            raise Exception(PAYMENT_BANK_NOT_FOUND,request.__dict__)

        userID = self._storage.getUserID(request.userName)
        if userID is None:
            raise Exception(PAYMENT_USER_NOT_FOUND,request.__dict__)

        userObject = self._storage.getUserObject(userID)
        loanID = userObject.hasLoanInBank(bankID)
        if not loanID:
            raise Exception(LOAN_NOT_TAKEN,request.__dict__)

        payment = Payment(request.amount)
        loanObject = self._storage.getLoanObject(loanID)
        amount_paid, emisLeft = loanObject.getBalance(request.emi_no)
        if emisLeft:
            self._storage.addPayment(payment)
            loanObject.addPayment(request.amount,request.emi_no)
        else:
            print(ZERO_EMIS_LEFT,request.__dict__)
