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
        tokens = request.split()
        self.__request_type = commandType.__members__.get(tokens[0])
        if self.__request_type and self.__request_type.value == len(tokens):
            self.__transaction.update(True, self.__request_type)
            self.__payloadDTO(tokens)
        else:
            raise ValueError(f"{INPUT_FORMAT_ERROR}: {request}")

    def getType(self):
        return self.__request_type

    def __payloadDTO(self, tokens):
        hmap = {'cmdType': self.__request_type}
        if self.__request_type == commandType.LOAN:
            for param in range(1, commandType.LOAN.value):
                hmap[LOAN_KEYS[param - 1]] = tokens[param]
            self.__request = LoanPayloadDTO(**hmap)
        elif self.__request_type == commandType.PAYMENT:
            for param in range(1, commandType.PAYMENT.value):
                hmap[PAYMENT_KEYS[param - 1]] = tokens[param]
            self.__request = PaymentPayloadDTO(**hmap)
        elif self.__request_type == commandType.BALANCE:
            for param in range(1, commandType.BALANCE.value):
                hmap[BALANCE_KEYS[param - 1]] = tokens[param]
            self.__request = BalancePayloadDTO(**hmap)

    def getRequestDTO(self):
        return self.__request
