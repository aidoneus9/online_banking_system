class Account:

    bank_name: str = "" # Optional[str]  None

    def __init__(self) -> None:
        self.__balance = 0
        self.transactions = [] 

    def deposit(self, amount: int) -> None: 

        if isinstance(amount, int) and amount > 0:
            self.__balance += amount 
            self.transactions.append(amount) # extend()
            print(f"입금: {amount}원")
            
        else:
            print("입금 실패")

    def withdrawal(self, amount: int) -> None:
        if isinstance(amount, int) and amount > 0 and amount <= self.__balance:
            self.__balance -= amount 
            self.transactions.append(-amount)
            print(f"출금: {amount}원")

        else:
            print("출금 실패")


    def get_balance(self) -> int: # 잔고 반환 
        return self.__balance
  
    def get_transactions(self) -> list: # 거래 내역 반환 
        return self.transactions

    @classmethod
    def get_bank_name(cls) -> str:
        return cls.bank_name

    @classmethod
    def set_bank_name(cls, name: str) -> None:
        cls.bank_name = name

