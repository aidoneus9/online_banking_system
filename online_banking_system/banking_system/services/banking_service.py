class BankingService:
    def __init__(self, users: list) -> None: # users: 사용자 목록을 저장하는 리스트 
        self.users  = users # 사용자 목록을 초기화 

    def add_user(self, username: str) -> None: # 사용자를 추가
        user = User(username) 
        self.users += [user]
        # ✏️ BankingService 클래스가 self.users 리스트를 통해 여러 User 객체를 관리함.
        # 각 User 객체는 username이라는 속성을 가지고 있으며, BankingService 클래스에서 접근할 수 있음.
        

    def find_user(self, username: str) -> User: # 사용자 찾기
        for user in self.users:
            if user.username == username: # -> 따라서 BankingService는 사용자 목록에서 User 객체를 찾아 그 객체의 username 속성에 접근하고 비교할 수 있음. 
                return user 
            raise ValueError("예외를 발생시킴")

    def user_menu(self, username: str) -> None: # 사용자 메뉴 제공 
    # - 사용자를 찾고, 1. 입금, 2. 출금, 3. 잔고 확인, 4. 거래 내역 기능  을 제공하는 반복 루프를 구현합니다.

    # - amount: 입금 또는 출금 금액을 나타내는 정수
    # - choice: 사용자의 선택을 나타내는 문자열

        if BankingService().find_user():
            while True:
                if choice == "종료":
                    print("서비스 종료")
                    break

                if choice == "1":
                    deposit()

                if choice == "2":
                    withdrawal()

                if choice == "3":
                    get_balance()

                if choice == "4":
                    get_transactions()

        else:
            
