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
###########################################################################
class Transaction: # ✅
    def __init__(self, transaction_type: str, amount: int, balance: int) -> None:
        self.transaction_type = transaction_type # 거래 유형을 나타내는 문자열 (예: 입금, 출금 )
        self.amount = amount  
        self.balance = balance

    def __str__(self) -> str: # 거래 정보를 문자열로 반환 
        return f'{self.transaction_type}: {self.amount}원, 잔액: {self.balance}원'

    def to_tuple(self) -> tuple: # 거래 정보를 튜플로 반환  
        return (self.transaction_type, self.amount, self.balance)
##################################################    
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
##################################################
class User: # ✅
    def __init__(self, username: str) -> None:
        self.username = username
        self.account = Account() # 직접 객체 생성 
##################################################
class BankingService:
    def __init__(self) -> None: # users: 사용자 목록을 저장하는 리스트 
        self.users: list[User] = [] # 사용자 목록을 초기화 

    def add_user(self, username: str) -> None: # 사용자를 추가
        user = User(username) # 1. User 인스턴스를 하나 생성 
        self.users.append(user) # 2. 그 인스턴스를 users 리스트에 저장
        # ✏️ BankingService 클래스가 self.users 리스트를 통해 여러 User 객체를 관리함.
        # 각 User 객체는 username이라는 속성을 가지고 있으며, BankingService 클래스에서 접근할 수 있음.
        print(f"{username}님이 등록되었습니다.")

    def find_user(self, username: str) -> User: # 사용자 찾기 # 3. 리스트를 돌면서 username이 일치하는 User 인스턴스를 찾아서 반환 
        for user in self.users:
            if user.username == username: # -> 따라서 BankingService는 사용자 목록에서 User 객체를 찾아 그 객체의 username 속성에 접근하고 비교할 수 있음. 
                return user 
        raise UserNotFoundError(username)

    def user_menu(self, username: str) -> None: # 사용자 메뉴 제공 

        # 🔍 사용자 찾기
        # 🤔 main()에서 이미 사용자를 찾고 user_menu()를 실행하는데 왜 user_menu() 안에서 다시 사용자 찾기가 필요한가?
        # -> main()에서 사용자를 찾는 코드는 있지만, 실제로는 User 객체를 반환받지 않았기 때문에 user_menu() 내부에서는 여전히 User 객체를 다시 찾아야 함. 
        try:
            user = self.find_user(username) # 4. 그 User 인스턴스를 user 변수에 저장
            # 6. ‼️ User 클래스에 직접 접근하는 게 아니라, self.users 리스트에서 이미 생성된 User 인스턴스를 꺼내오는 것임!
        except UserNotFoundError:
            print("사용자를 찾을 수 없습니다.")
        
        while True: 
         
         print("[1] 입금 [2] 출금 [3] 잔액 확인 [4] 거래 내역 [5] 종료")
         choice = input("원하시는 서비스의 번호를 입력해 주세요: ")

         if choice not in ["1", "2", "3", "4", "5"]:
            print("1에서 5까지의 숫자 중 하나를 입력해 주세요.")
            continue
 
         # 종료 조건 
         if choice == "5":
            print("서비스 종료 중...")
            break

         if choice == "1":
            amount = int(input("입금할 금액을 입력하세요: "))
            user.account.deposit(amount) # 5. 와 같은 방식으로 클래스 속성 사용 가능

         if choice == "2":
            amount = int(input("출금할 금액을 입력하세요: "))
            user.account.withdrawal(amount)

         if choice == "3":
            print(f'현재 잔액: {user.account.get_balance()}원')
            
         if choice == "4":
            print("=====🧾 거래 내역=====")
            user.account.get_transactions()
##################################################
def main() -> None:
    banking_service = BankingService()

    print("[1] 사용자 추가 [2] 사용자 찾기 [3] 종료")
    service_number = input("원하시는 서비스의 번호를 입력해 주세요: ")
    
    if service_number not in ["1", "2", "3"]:
        main()
    
    if service_number == "3":
        print("서비스 종료 중...")
        return # 함수라서 break 안 씀 

    if service_number == "1":
        username = input("이름을 입력해 주세요: ")
        banking_service.add_user(username) 

    if service_number == "2":
        banking_service.find_user(username)
        # find_user(username)을 호출하긴 했지만, return 값을 저장하지 않았음.
        # user_menu(username) 함수는 단순히 문자열(username)만 전달받음.
        # -> user_menu() 안에서는 그 username을 가지고 다시 User 객체를 찾는 작업이 필요함. 

    banking_service.user_menu(username)

if __name__ == "__main__":
    main() 

