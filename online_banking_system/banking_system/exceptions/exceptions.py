# 사용자 정의 예외 클래스 ‼️  
class InsuccicientFundsError(Exception): # Exception 클래스 상속 
    def __init__(self, balance: int) -> None:
        super().__init__(f"잔액 부족 \t 현재 잔액: {balance}원")

class NegativeAmountError(Exception):
    def __init__(self) -> None:
        super().__init__("입금 또는 출금하실 금액은 0원보다 커야 합니다.")

class UserNotFoundError(Exception):
    def __init__(self, username:str) -> None:
        super().__init__(f"입력하신 사용자 '{username}'을/를 찾을 수 없습니다.")
#########################################################################
# 거래 유효성 검사 데코레이터 구현 
from typing import Callable

def validate_transaction(func: Callable) -> Callable: # function은 deposit / withdrawal 함수
    def wrapper(self, amount:int) -> None:
        if amount <= 0:
            raise NegativeAmountError()
        return func(self, amount)
    return wrapper # wrapper 함수가 먼저 실행되도록 함.

