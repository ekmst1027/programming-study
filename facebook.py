class Facebook:
    def __init__(self, first_name, last_name, mobile, email):
        self.first_name = first_name
        self.last_name = last_name
        self.mobile = mobile
        self.email = email

    def printAll(self):
        print('first_name: ' + self.first_name)
        print('last_name: ' + self.last_name)
        print('mobile: ' + self.mobile)
        print('email: ' + self.email)\

    def main():
        print("Choose the menu you wnat below:")
        print("1:create   2:read all   3:read by condition   4:exit")
        try:
            number = int(input("choose your menu>>")) # 선택할 메뉴
        # 숫자가 아닐때 예외처리
        except ValueError:
            print("please choose one of 1,2,3,4")
            main()

        if number == 1:
            first_name = input("What's your first name?")
            last_name = input("What's your last name?")
            mobile = input("What's your mobile phone number?")
            email = input("What's your email address?")

            info = [first_name, last_name, mobile, email]
            a = Facebook(info)
            print("입력완료")

        elif number == 2:
            Facebook.printAll()


    if __name__ == "__main__" :
        main()
