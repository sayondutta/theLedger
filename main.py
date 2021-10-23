from src.util.constants import INPUT_FILE
from src.impl.inMemStorage import Storage
from src.util.queryparser import QueryParser
from src.dto.enums.commandType import commandType
from src.controller.loancontroller import LoanController
from src.controller.paymentcontroller import PaymentController
from src.controller.balancecontroller import BalanceController

def start():
    storage = Storage()

    loanController = LoanController(storage)
    paymentController = PaymentController(storage)
    balanceController = BalanceController(storage)

    f = open(INPUT_FILE,'r')
    while True:
        request = f.readline()
        if len(request)==0:
            f.close()
            break
        parsed_request = QueryParser(request,storage)
        request_type = parsed_request.getType()
        if request_type:
            requestDTO = parsed_request.getRequestDTO()
            if request_type == commandType.LOAN:
                loanController.processRequest(requestDTO)
            elif request_type == commandType.PAYMENT:
                paymentController.processRequest(requestDTO)
            elif request_type == commandType.BALANCE:
                balanceController.processRequest(requestDTO)


if __name__ == "__main__":
    start()