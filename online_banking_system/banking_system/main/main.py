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
