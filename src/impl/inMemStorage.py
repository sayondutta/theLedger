from collections import defaultdict
from src.dto.entities.transaction import Transaction
from src.dto.entities.user import User
from src.dto.entities.bank import Bank
from src.dto.entities.loan import Loan
from src.dto.entities.payment import Payment


class Storage:
    def __init__(self):
        # defaultdict is Thread Safe
        self.__transactionStore = defaultdict(Transaction) # transaction storage {<key> transactionID : <value> transactionObject}
        self.__userStore = defaultdict(User)  # user storage {<key> userID : <value> userObject}
        self.__bankStore = defaultdict(Bank) # bank storage {<key> bankID : <value> bankObject}
        self.__loanStore = defaultdict(Loan) # loan storage {<key> loanID : <value> loanObject}
        self.__paymentStore = defaultdict(Payment) # payment storage {<key> paymentID : <value> paymentObject}
        self.__userNameIdMap = defaultdict(str) # {<key> userName : <value> userID}
        self.__bankNameIdMap = defaultdict(str) # {<key> bankName : <value> bankID}

    def addBank(self,bank):
        '''
        Adds new bank to bank store
        :param bank: bank object
        '''
        self.__bankStore[bank.getBankID()] = bank

    def addLoan(self,loan):
        '''
        Adds new loan to loan store
        :param loan: loan object
        '''
        self.__loanStore[loan.getLoanID()] = loan

    def addUser(self,user):
        '''
        Adds new user to user store
        :param user: user object
        '''
        self.__userStore[user.getUserID()] = user

    def addPayment(self,payment):
        '''
        Adds new payment to payment store
        :param payment: payment object
        '''
        self.__paymentStore[payment.getPaymentID()] = payment

    def addTransaction(self,transaction):
        '''
        Adds new transaction to transaction store
        :param transaction: transaction object
        '''
        self.__transactionStore[transaction.getTransactionID()] = transaction

    def getBankID(self,name):
        '''
        :param name: bankName
        :return: bankID
        '''
        return self.__bankNameIdMap.get(name,None)

    def getUserID(self,name):
        '''
        :param name: userName
        :return: userID
        '''
        return self.__userNameIdMap.get(name,None)

    def putBank(self,bankName,bankID):
        '''
        Adds the pair (bankName,bankID) to bankNameIdMap
        :param bankName: bank name
        :param bankID: bankID
        '''
        self.__bankNameIdMap[bankName] = bankID

    def putUser(self,userName,userID):
        '''
        Adds the pair (userName,userID) to userNameIdMap
        :param userName: user name
        :param userID: userID
        '''
        self.__userNameIdMap[userName] = userID

    def getUserObject(self,userID):
        '''
        :param userID: userID
        :return: userObject
        '''
        return self.__userStore[userID]

    def getLoanObject(self,loanID):
        '''
        :param loanID: loanID
        :return: loanObject
        '''
        return self.__loanStore[loanID]
