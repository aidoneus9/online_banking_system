# 데코레이터 구현

from typing import Callable

def validate_transaction(func: Callable) -> Callable:
    if amount > 0:
        return True
    return False 

# 사용자 정의 예외 클래스
class InsuccicientFundsError(Exception):
    def __init__(self, balance: int) -> None:
        self.balance = balance

class NegativeAmountError(Exception):
    def __init__(self) -> None:

class UserNotFoundError(Exception):
    def __init__(self, username:str) -> None

