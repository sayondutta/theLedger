from collections import defaultdict
from src.dto.entities.transaction import Transaction
from src.dto.entities.user import User
from src.dto.entities.bank import Bank
from src.dto.entities.loan import Loan
from src.dto.entities.payment import Payment


class Storage:
    def __init__(self):
        self.__transactionStore = defaultdict(Transaction)
        self.__userStore = defaultdict(User)
        self.__bankStore = defaultdict(Bank)
        self.__loanStore = defaultdict(Loan)
        self.__paymentStore = defaultdict(Payment)
        self.__userNameIdMap = defaultdict(str)
        self.__bankNameIdMap = defaultdict(str)

    def addBank(self,bank):
        self.__bankStore[bank.getBankID()] = bank

    def addLoan(self,loan):
        self.__loanStore[loan.getLoanID()] = loan

    def addUser(self,user):
        self.__userStore[user.getUserID()] = user

    def addPayment(self,payment):
        self.__paymentStore[payment.getPaymentID()] = payment

    def addTransaction(self,transaction):
        self.__transactionStore[transaction.getTransactionID()] = transaction

    def getBankID(self,name):
        return self.__bankNameIdMap.get(name,None)

    def getUserID(self,name):
        return self.__userNameIdMap.get(name,None)

    def putBank(self,bankName,bankID):
        self.__bankNameIdMap[bankName] = bankID

    def putUser(self,userName,userID):
        self.__userNameIdMap[userName] = userID

    def getUserObject(self,userID):
        return self.__userStore[userID]

    def getLoanObject(self,loanID):
        return self.__loanStore[loanID]
