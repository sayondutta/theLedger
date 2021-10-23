import uuid


class Transaction:
    def __init__(self, request):
        self.__id = uuid.uuid1()
        self.__request = request
        self.__type = None
        self.__isValid = False

    def getTransactionID(self):
        return self.__id

    def update(self, status, request_type):
        self.__isValid = status
        self.__type = request_type
