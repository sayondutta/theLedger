import uuid

class Payment:
    def __init__(self,amount):
        self.__id = uuid.uuid1()
        self.__amount = amount

    def getPaymentID(self):
        return self.__id

