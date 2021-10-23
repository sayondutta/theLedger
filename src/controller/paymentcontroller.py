from src.controller.controller import BaseController
from src.util.constants import PAYMENT_BANK_NOT_FOUND, PAYMENT_USER_NOT_FOUND, LOAN_NOT_TAKEN
from src.dto.entities.payment import Payment


class PaymentController(BaseController):
    def __init__(self, storage):
        super().__init__(storage)

    def processRequest(self, request):
        bankID = self._storage.getBankID(request.bankName)
        if bankID is None:
            raise ValueError(PAYMENT_BANK_NOT_FOUND)

        userID = self._storage.getUserID(request.userName)
        if userID is None:
            raise ValueError(PAYMENT_USER_NOT_FOUND)

        userObject = self._storage.getUserObject(userID)
        loanID = userObject.hasLoanInBank(bankID)
        if not loanID:
            raise ValueError(LOAN_NOT_TAKEN)

        payment = Payment(request.amount)
        self._storage.addPayment(payment)
        self._storage.getLoanObject(loanID).addPayment(request.amount,request.emi_no)
