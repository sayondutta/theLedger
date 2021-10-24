from src.controller.controller import BaseController
from src.dto.entities.bank import Bank
from src.dto.entities.user import User
from src.dto.entities.loan import Loan
from src.util.constants import LOAN_ALREADY_IN_THE_BANK


class LoanController(BaseController):
    def __init__(self, storage):
        super().__init__(storage)

    def processRequest(self, request):
        # if user and bank not in storage: create user and bank object
        bankID = self._storage.getBankID(request.bankName)
        if bankID is None:
            bank = Bank(request.bankName)
            self._storage.addBank(bank)
            bankID = bank.getBankID()
            self._storage.putBank(request.bankName, bankID)

        userID = self._storage.getUserID(request.userName)
        if userID is None:
            user = User(request.userName)
            self._storage.addUser(user)
            userID = user.getUserID()
            self._storage.putUser(request.userName, userID)

        userObject = self._storage.getUserObject(userID)
        if userObject.hasLoanInBank(bankID):
            raise Exception(LOAN_ALREADY_IN_THE_BANK,request.__dict__)

        # create loan object
        loan = Loan(request.principal, request.years, request.rate)
        self._storage.addLoan(loan)
        userObject.addBankID(bankID, loan.getLoanID())
