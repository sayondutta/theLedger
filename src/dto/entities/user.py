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
        '''
        Adds the {bankID: loanID} key-value to self.__banks dictionary
        :param bankID: bank ID
        :param loanID: loan ID
        '''
        self.__banks[bankID] = loanID

    def hasLoanInBank(self, bankID):
        '''
        Checks if the user has loan in the queried bank
        :param bankID: bank ID
        :return: loanObject or None
        '''
        return self.__banks.get(bankID,None)