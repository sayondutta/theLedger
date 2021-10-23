import uuid
from collections import defaultdict

class Bank:
    def __init__(self,name):
        self.__id = uuid.uuid1()
        self.__name = name

    def getBankID(self):
        return self.__id