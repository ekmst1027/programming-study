class Facebook:
    def __init__(self, first_name, last_name, mobile, email):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__mobile = mobile
        self.__email = email

    def printAll(self):
        print('first_name: ' + self.__first_name)
        print('last_name: ' + self.__last_name)
        print('mobile: ' + self.__mobile)
        print('email: ' + self.__email)
        print()

ws = Facebook("wan-sup", "cho", "123", "wscho@gmail.com")
ws.printAll()





# def print_menu():
#     print("Choose the menu you want below:")
#     print("1:create   2:read all   3:read by condition   4:exit")
#     number = int(input("choose your menu>>")) # 선택할 메뉴
#     return number
#
# def set_info():
#     first_name = input("What's your first name?")
#     last_name = input("What's your last name?")
#     mobile = input("What's your mobile?")
#     email = input("What's your email?")
#     person = Facebook(first_name, last_name, mobile, email)
#     return person
#
# def print_info(people):
#     for person in people:
#         person.printAll()
#
# def search_info(people):
#     keyword = input('what keyword do you want to search?')
#
#     for person in people:
#         person_list = [person.first_name, person.last_name, person.mobile, person.email]
#         if keyword in person_list:
#             search[person.mobile] = keyword
#
#     mobile_list = list(search.keys())
#     new_list = []
#     for person in people:
#         if person.mobile in mobile_list:
#             new_list.append(person)
#
#     if len(mobile_list) == 0:
#         print("There is no item")
#     else:
#         print("\nThere is(are) {} item(s)\n".format(len(mobile_list)))
#         print_info(new_list)
#
# def main():
#     # a = Facebook("lee", "km", "123", "asdfas")
#     # b = Facebook("km", "lee", "456", "bvdsa")
#     # c = Facebook("cho", "ws", "2525", "lee")
#     # d = Facebook("ws", "cho", "64", "okjawef")
#     # people = [a, b, c, d] # test data
#     people = []
#     search = {}
#     while True:
#         print()
#         try:
#             number = int(print_menu())
#         except ValueError:
#             print("please choose one of 1,2,3,4")
#             continue
#         if number == 1:
#             person = set_info()
#             people.append(person)
#
#         elif number == 2:
#             print_info(people)
#
#         elif number == 3:
#             search_info(people)
#
#         elif number == 4:
#             break
#         else:
#             print("please choose one of 1,2,3,4")
#             continue
#
# if __name__ == "__main__" :
#     main()


# print("first_name: wan-sup")
# print("last_name: cho")
# print("mobile: 123")
# print("email: wscho@gmail.com")
# print()
# print("first_name: yeo-pyo")
# print("last_name: yoon")
# print("mobile: 111")
# print("email: yp@cbnu.ac.kr")
# print()
# print("first_name: jae-in")
# print("last_name: moon")
# print("mobile: 000")
# print("email: ji@naver.com")
