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