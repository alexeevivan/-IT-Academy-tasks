import os
import functools
from time import sleep
from colorama import init
from colorama import Fore, Back, Style


# «L.V.19 LLC» - случайное название компании в качестве примера
a = ("A list of employees of the company «L.V.19 LLC».")
b = ("Documentation related to taxation issues of the company «L.V.19 LLC».")
c = ("Constituent documents (articles of association, licenses, etc.)")

welcome_message = ("\nWelcome to the «About us» section.")
# ознакомительная информация
menu_list_introductory = """
\n1. A list of employees of the company «L.V.19 LLC»
— — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — 
\n2. Documentation related to taxation issues of the company «L.V.19 LLC»
— — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — 
\n3. Constituent documents (articles of association, licenses, etc.)
— — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — 
"""
# информация, доступная после успешного входа
menu_list_main = """
\n1. A list related to the employees of the company «L.V.19 LLC»
— — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — 
\n\t1.1 «L.V.19 LLC» list of employees by the position
\n\t1.2 «L.V.19 LLC» employees salary list by the position
\n\t1.3 «L.V.19 LLC» employees certification results
— — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — 
\n2. Documentation related to taxation issues of the company «L.V.19 LLC»
— — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — 
\n3. Constituent documents (articles of association, licenses, etc.)
— — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — 
"""
usernames = ["Ivan", "Julia", "Ian"]
user_1 = usernames[0]
user_2 = usernames[1]
user_3 = usernames[2]
keys = [1, 2, 3]
key_1 = keys[0]
key_2 = keys[1]
key_3 = keys[2]

print(welcome_message, Fore.MAGENTA, menu_list_introductory, Fore.WHITE)

expaining_message = ("For further viewing of the information provided below, please complete the authentication procedeure.")
print(expaining_message)
request_message_2 = int(input("\nPlease enter 1 to continue:"))
while request_message_2!=1:
    print(Fore.RED, "An invalid response was entered. Try again or return to homepage.", Fore.WHITE)
    request_message_2 = int(input("\nPlease enter 1 to log in:"))
if request_message_2==1:
    os.system('cls' if os.name=='nt' else 'clear')


# проверка имени пользователя
def userask(func):
    def wrapper():
        print(Fore.GREEN,"Got it.", Fore.WHITE)
        sleep(2)
        os.system('cls' if os.name=='nt' else 'clear')
    return wrapper


# проверка пароля
def pass_ask(func):
    def wrapper_1():
        print(Fore.GREEN,"Got it.", Fore.WHITE)
        sleep(2)
        os.system('cls' if os.name=='nt' else 'clear')
    return wrapper_1


username_request = str.title(input("Please enter your nickname:"))
if username_request in usernames:
    @userask
    def login(usernames):
        pass
    login()
else:
    print(Fore.RED,"\nOops. Nice try, but it is the place with no errors in typing allowed!", Fore.WHITE)
    StopIteration


def pass_ask(func):
    def wrapper_1():
        print(Fore.GREEN,"Got it.", Fore.WHITE)
        sleep(2)
        os.system('cls' if os.name=='nt' else 'clear')
    return wrapper_1


if username_request in usernames:
    password_request = int(input("Enter the password:"))
    if password_request==keys[0] and username_request==user_1:
        @pass_ask
        def login_2_step(keys):
            pass
        login_2_step()
        print(Fore.GREEN,"\nNow you are able to discover the files i have.", Fore.CYAN, menu_list_main)
    elif password_request==keys[1] and username_request==user_2:
        @pass_ask
        def login_2_step(keys):
            pass
        login_2_step()
        print(Fore.GREEN,"\nNow you are able to discover the files i have.", Fore.CYAN, menu_list_main)
    elif password_request==keys[2] and username_request==user_3:
        @pass_ask
        def login_2_step(keys):
            pass
        login_2_step()
        print(Fore.GREEN,"\nNow you are able to discover the files i have.", Fore.CYAN, menu_list_main)
    else:
        os.system('cls' if os.name=='nt' else 'clear')
        print(Fore.RED, "\nOops. Nice try, but it is the place with no errors in typing allowed!", Fore.WHITE)
        StopIteration
else:
    StopIteration