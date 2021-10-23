import uuid

class User:
    def __init__(self, name):
        self.__id = uuid.uuid1()
        self.__name = name
        self.__banks = {}

    def getUserID(self):
        return self.__id

    def getUserName(self):
        return self.__name

    def addBankID(self, bankID, loanID):
        self.__banks[bankID] = loanID

    def hasLoanInBank(self, bankID):
        return self.__banks.get(bankID,None)