class User: # ✅
    def __init__(self, username: str) -> None:
        self.username = username
        self.account = Account() # 직접 객체 생성 