from src.dto.enums.commandType import commandType
from src.dto.entities.transaction import Transaction
from src.util.constants import INPUT_FORMAT_ERROR, LOAN_KEYS, PAYMENT_KEYS, BALANCE_KEYS
from src.dto.payload.payload import LoanPayloadDTO, PaymentPayloadDTO, BalancePayloadDTO

class QueryParser:
    def __init__(self, request, storage):
        self.__transaction = Transaction(request)
        self.__request_type = False
        self.__request = None
        self.__runParser(request)
        storage.addTransaction(self.__transaction)

    def __runParser(self, request):
        '''
        Evaluates the request string is valid and if valid sent to parse payload to DTO
        :param request: request string
        '''
        tokens = request.split()
        self.__request_type = commandType.__members__.get(tokens[0])   # type : LOAN/PAYMENT/BALANCE else Null
        if self.__request_type and self.__request_type.value == len(tokens): # if length matches the desired length of the request_type
            self.__payloadDTO(tokens)
        else:
            raise Exception(INPUT_FORMAT_ERROR,request)

    def getType(self):
        '''
        :return: <commandType.LOAN: 6> / <commandType.PAYMENT: 5> / <commandType.BALANCE: 4> / False (default)
        '''
        return self.__request_type

    def __payloadDTO(self, tokens):
        '''
        :param tokens: tokens of strings (of the actual string request)
        '''
        hmap = {'cmdType': self.__request_type}  # changes request to hashmap of {param_value: param_value}
        if self.__request_type == commandType.LOAN:
            for param in range(1, commandType.LOAN.value):
                hmap[LOAN_KEYS[param - 1]] = tokens[param]
            try:
                self.__request = LoanPayloadDTO(**hmap)  # convert hashmap to Loan DTO
                self.__transaction.update(True, self.__request_type)  # update transaction to be valid
            except:
                raise Exception(INPUT_FORMAT_ERROR,tokens)
        elif self.__request_type == commandType.PAYMENT:
            for param in range(1, commandType.PAYMENT.value):
                hmap[PAYMENT_KEYS[param - 1]] = tokens[param]
            try:
                self.__request = PaymentPayloadDTO(**hmap) # convert hashmap to Payment DTO
                self.__transaction.update(True, self.__request_type)  # update transaction to be valid
            except:
                raise Exception(INPUT_FORMAT_ERROR,tokens)
        elif self.__request_type == commandType.BALANCE:
            for param in range(1, commandType.BALANCE.value):
                hmap[BALANCE_KEYS[param - 1]] = tokens[param]
            try:
                self.__request = BalancePayloadDTO(**hmap) # convert hashmap to Balance DTO
                self.__transaction.update(True, self.__request_type)  # update transaction to be valid
            except:
                raise Exception(INPUT_FORMAT_ERROR,tokens)

    def getRequestDTO(self):
        '''
        :return: requestDTO
        '''
        return self.__request
