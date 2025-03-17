class Account: # ✅

    bank_name: str = "" # bank_name: Optional[str] = None

    def __init__(self) -> None:
        self.__balance = 0
        self.transactions: list[Transaction] = []

    @validate_transaction # 데코레이터 (amount > 0)
    def deposit(self, amount: int) -> None:
        #if isinstance(amount, int) and amount > 0:
        self.__balance += amount 
        self.transactions.append(Transaction("입금", amount, self.__balance)) # extend()
        print(f"입금: {amount}원")
            
    @validate_transaction # 데코레이터 (amount > 0)
    def withdrawal(self, amount: int) -> None:
        # if isinstance(amount, int) and amount > 0 and amount <= self.__balance:
        if amount > self.__balance:
            raise InsuccicientFundsError()
        self.__balance -= amount 
        self.transactions.append(Transaction("출금", amount, self.__balance))
        print(f"출금: {amount}원")

    def get_balance(self) -> int: # 잔고 반환 
        return self.__balance
  
    def get_transactions(self) -> list: # 거래 내역 반환 
        if not self.transactions:
            print("거래 내역이 없습니다.")
        for transaction in self.transactions:
            print(transaction)

    @classmethod # <- 어디다가 쓰는 거야? 
    def get_bank_name(cls) -> str:
        return cls.bank_name

    @classmethod
    def set_bank_name(cls, name: str) -> None:
        cls.bank_name = name