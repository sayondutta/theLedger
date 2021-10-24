import uuid
import math


class Loan:

    def __init__(self, principal, time, rate):
        self.__principal = principal
        self.__time = time
        self.__rate = rate
        self.__id = uuid.uuid1()
        self.__payments = {}  # key value pair {emi_no : (payment ID, payment amount}

    def getLoanID(self):
        return self.__id

    def addPayment(self, paymentID, paymentAmt, emi_no):
        '''
        Adds payment associated to this loan
        :param paymentID: payment ID
        :param paymentAmt: lumpsum payment amount
        :param emi_no: EMI counter after which this lumpsum payment is added
        '''
        self.__payments[emi_no] = (paymentID,paymentAmt)

    def getBalance(self,emi_no):
        '''
        :param emi_no: EMI counter after which the balance query is called
        :return: total amount repaid, total number of EMIs remaining
        '''
        maturityAmount = math.ceil(self.__principal * (1 + (self.__time * self.__rate) / 100)) # A = P * (1+ R*T/100)
        emiVal = math.ceil(maturityAmount / (self.__time *12)) # A / (12*T)
        amount_repaid = 0
        counter = 0
        while counter < emi_no and amount_repaid < maturityAmount:
            amount_repaid += emiVal
            amount_repaid += self.__payments.get(counter+1, (0,0))[1]
            counter += 1

        emis_remaining = math.ceil(max(0,maturityAmount-amount_repaid)/emiVal)
        return int(amount_repaid),emis_remaining
