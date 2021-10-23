from pydantic import BaseModel
from src.dto.enums.commandType import commandType


class LoanPayloadDTO(BaseModel):
    cmdType: commandType
    bankName: str
    userName: str
    principal: float
    years: float
    rate: float


class PaymentPayloadDTO(BaseModel):
    cmdType: commandType
    bankName: str
    userName: str
    amount: float
    emi_no: int


class BalancePayloadDTO(BaseModel):
    cmdType: commandType
    bankName: str
    userName: str
    emi_no: int
