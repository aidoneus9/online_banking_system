
class Transaction:
    def __init__(self, transaction_type: str, amount: int, balance: int) -> None:
        self.transaction_type = transaction_type # 거래 유형을 나타내는 문자열 (예: 입금, 출금 )
        self.amount = amount  
        self.balance = balance

    def __str__(self) -> str: # 거래 정보를 문자열로 반환 
        return 

    def to_tuple(self) -> tuple: # 거래 정보를 튜플로 반환  
        return 

