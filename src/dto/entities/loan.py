import uuid
import math


class Loan:

    def __init__(self, principal, time, rate):
        self.__principal = principal
        self.__time = time
        self.__rate = rate
        self.__id = uuid.uuid1()
        self.__payments = {}

    def getLoanID(self):
        return self.__id

    def addPayment(self, paymentID, emi_no):
        self.__payments[emi_no] = paymentID

    def getBalance(self,emi_no):
        maturityAmount = math.ceil(self.__principal * (1 + (self.__time * self.__rate) / 100))
        emiVal = math.ceil(maturityAmount / (self.__time *12))
        amount_repaid = emi_no*emiVal
        for key in self.__payments:
            if key<=emi_no:
                amount_repaid += self.__payments[key]
        emis_remaining = math.ceil(max(0,maturityAmount-amount_repaid)/emiVal)
        return int(amount_repaid),emis_remaining
