import os
from colorama import init
from colorama import Fore, Back, Style


j = ("\nВас приветствует игра «-Tic-Tac-Toe-» !!! \nКаждая ячейка выделена цифровым индикатором для удобства планирования ходов.")
b2 = """
     |     |                  |     |   
  ■  |  ■  |  ■            1  |  2  |  3  
     |     |                  |     |    
— — — — — — — — —         — — — — — — — — —
     |     |                  |     |   
  ■  |  ■  |  ■            4  |  5  |  6  
     |     |                  |     |     
— — — — — — — — —         — — — — — — — — —
     |     |                  |     |   
  ■  |  ■  |  ■            7  |  8  |  9  
     |     |                  |     |
— — — — — — — — —         — — — — — — — — — 
"""


print(j)
print(Fore.MAGENTA, b2)


print(Fore.WHITE)
player_1 = str.title(input("Введите имя первого игрока:"))
player_2 = str.title(input("\nВведите имя второго игрока:"))
p_1, p_2  = player_1, player_2


print(Fore.LIGHTCYAN_EX)
print("Приветствую,", player_1, "и", player_2, "!")
x = ("X")
o = ("O")
c = ("Отлично! Игрок")
d = ("использует символ X. Осталось совсем чуть-чуть.")
e = ("использует символ O. Пора начинать.")



print(Fore.WHITE)
f = int(input("Введите «1», если игрок №1 желает использовать символ Х, или «2» - если будет использовать символ О:"))
print(Fore.LIGHTCYAN_EX)
while f!=1 and f>2:
    print("Введён некорректный ответ. Попробуйте ещё раз.")
    f = int(input("Введите «1», если игрок №1 желает использовать символ Х, или «2» - если будет использовать символ О:"))
if f==1:
    print(c, p_1, d)
if f==2:
    print(c, p_1, e)


print(Fore.WHITE)
g = int(input("Введите «1», если игрок №2 использует символ Х, или «2» - если использует символ О:"))
while g==f:
    print(Fore.RED)
    print("К сожалению, данный символ зарезервирован за игроком", player_1, ".")
    print(Fore.WHITE)
    g = int(input("Введите «1», если игрок №2 использует символ Х, или «2» - если использует символ О:"))
while g!=1 and g>2:
    print(Fore.RED)
    print("Введён некорректный ответ. Попробуйте ещё раз.")
    print(Fore.WHITE)
    g = int(input("Введите «1», если игрок №2 использует символ Х, или «2» - если использует символ О:"))
print(Fore.LIGHTCYAN_EX)
if g==1:
    print(c, p_2, d)
if g==2:
    print(c, p_2, e)


print(Fore.WHITE)
u = input("Как правило, первый ход совершает игрок, чьим символом является «Х». \nВ зависимости от выбранного Вами ответа («+» или «-») я пойму, желаете ли Вы следовать этому правилу:")
p = ("+")
p_1 = ("/'+'/")
p_2 = ('/"+"/')
p_3 = ("«+»")
p_4 = p or p_1 or p_2 or p_3
s = ("-")
s_1 = ("/'-'/")
s_2 = ('/"-"/')
s_3 = ("«-»")
s_4 = s or s_1 or s_2 or s_3
while (u!=p and u!=s) and (u!=p_1 and u!=s_1) and (u!=p_2 and u!=s_2) and (u!=p_3 and u!=s_3):
    print("Введён некорректный символ. Попробуйте ещё раз:")
    u = input("Как правило, первый ход совершает игрок, чьим символом является «Х». \nВ зависимости от выбранного Вами ответа («+» или «-») я пойму, желаете ли Вы следовать этому правилу:")
print(Fore.LIGHTCYAN_EX)
if ((u==p and f==1) or (u==p_1 and f==1) or (u==p_2 and f==1) or (u==p_3 and f==1)) or ((u!=p or u!=p_1 or u!=p_2 or u!=p_3) and g==2):
    print("Отлично. Игрок", p_1, "использует символ", x,"и начнёт игру первым!")
    print("Отлично. Игрок", p_2, "использует символ", o,"и начнёт игру вторым!")
elif ((u!=p and f==1) or (u!=p_1 and f==1) or (u!=p_2 and f==1) or (u!=p_3 and f==1)) or ((u==p or u==p_1 or u==p_2 or u==p_3) and g==2):
    print("Отлично. Игрок", p_2, "использует символ", o,"и начнёт игру первым!")
    print("Отлично. Игрок", p_1, "использует символ", x,"и начнёт игру вторым!")
elif ((u==p or u==p_1 or u==p_2 or u==p_3) and g==1) or ((u!=p or u!=p_1 or u!=p_2 or u!=p_3) and f==2):
    print("Отлично. Игрок", p_2, "использует символ", x,"и начнёт игру первым!")
    print("Отлично. Игрок", p_1, "использует символ", o,"и начнёт игру вторым!")
elif ((u!=p or u!=p_1 or u!=p_2 or u!=p_3) and g==1) or ((u==p or u==p_1 or u==p_2 or u==p_3) and f==2):
    print("Отлично. Игрок", p_1, "использует символ", o,"и начнёт игру первым!")
    print("Отлично. Игрок", p_2, "использует символ", x,"и начнёт игру вторым!")


print(Fore.MAGENTA, b2)
print(Fore.WHITE)


# сокращение до переменных выбора игрока
    # player_1 == X, player_2 == 0
xx_1 = int(((u==p and f==1) or (u==p_1 and f==1) or (u==p_2 and f==1) or (u==p_3 and f==1)) or ((u!=p or u!=p_1 or u!=p_2 or u!=p_3) and g==2))
    # player_1==O, player_2==X
xx_2 = int(((u!=p or u!=p_1 or u!=p_2 or u!=p_3) and g==1) or ((u==p or u==p_1 or u==p_2 or u==p_3) and f==2))
    # player_2==X, player_1==O
xx_3 = int(((u==p or u==p_1 or u==p_2 or u==p_3) and g==1) or ((u!=p or u!=p_1 or u!=p_2 or u!=p_3) and f==2))
    # player_2==O, player_1==X
xx_4 = int(((u!=p and f==1) or (u!=p_1 and f==1) or (u!=p_2 and f==1) or (u!=p_3 and f==1)) or ((u==p or u==p_1 or u==p_2 or u==p_3) and g==2))


win_combo = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]
board = list(range(1, 10))


def draw_board():
    for i in range(3):
        print("     |     |     ")
        print(" ", board[0 + i * 3], " | ", board[1 + i * 3], " | ", board[2 + i * 3])
        print("     |     |     ")
        print("— — — — — — — — —")


def take_input(player_token):
    while True:
        value = input("Введите номер ячейки для совершения хода:")
        if not (value in '123456789'):
            print("Введён некорректный символ. Попробуйте ещё раз:")
            continue
        value = int(value)
        if str(board[value - 1]) in "XO":
            print(Fore.RED)
            print("К сожалению, данная клетка уже занята Вашим оппонентом.игроком. Выберите пустую ячейку:")
            print(Fore.WHITE)
            continue
        board[value - 1] = player_token
        break


def check_win():
    for each in win_combo:
        if (board[each[0]-1]) == (board[each[1]-1]) == (board[each[2]-1]):
            return board[each[1]-1]
    else:
        return False


def main():
    counter = 0
    while True:
        if xx_1==True:
            os.system('cls' if os.name=='nt' else 'clear')
            print(Fore.MAGENTA)
            draw_board()
            print(Fore.WHITE)
            if counter % 2 == 0:
                take_input(x)
            else:
                take_input(o)
            if counter > 3:
                victory = check_win()
                if victory:
                    print(Fore.GREEN)
                    draw_board()
                    if victory==check_win() and victory==x:
                        print(Fore.BLUE)
                        print(player_1, "победил(-a!")
                        print(Fore.WHITE)
                        break
                    if victory==check_win() and victory==o:
                        print(Fore.BLUE)
                        print(player_2, "победил(-a!")
                        print(Fore.WHITE)
                        break
            counter += 1
            if counter > 8:
                draw_board()
                print(Fore.YELLOW)
                print("Ничья!")
                print(Fore.WHITE)
                break
        elif xx_2==True:
            os.system('cls' if os.name=='nt' else 'clear')
            print(Fore.MAGENTA)
            draw_board()
            print(Fore.WHITE)
            if counter % 2 == 0:
                take_input(o)
            else:
                take_input(x)
            if counter > 3:
                victory = check_win()
                if victory:
                    print(Fore.GREEN)
                    draw_board()
                    if victory==check_win() and victory==o:
                        print(Fore.BLUE)
                        print(player_1, "победил(-a!")
                        print(Fore.WHITE)
                        break
                    if victory==check_win() and victory==x:
                        print(Fore.BLUE)
                        print(player_2, "победил(-a!")
                        print(Fore.WHITE)
                        break
            counter += 1
            if counter > 8:
                draw_board()
                print(Fore.YELLOW)
                print("Ничья!")
                print(Fore.WHITE)
                break
        elif xx_3==True:
            os.system('cls' if os.name=='nt' else 'clear')
            print(Fore.MAGENTA)
            draw_board()
            print(Fore.WHITE)
            if counter % 2 == 0:
                take_input(x)
            else:
                take_input(o)
            if counter > 3:
                victory = check_win()
                if victory:
                    print(Fore.GREEN)
                    draw_board()
                    if victory==check_win() and victory==x:
                        print(Fore.BLUE)
                        print(player_2, "победил(-a!")
                        print(Fore.WHITE)
                        break
                    if victory==check_win() and victory==o:
                        print(Fore.BLUE)
                        print(player_1, "победил(-a!")
                        print(Fore.WHITE)
                        break
            counter += 1
            if counter > 8:
                draw_board()
                print(Fore.YELLOW)
                print("Ничья!")
                print(Fore.WHITE)
                break
        elif xx_4==True:
            os.system('cls' if os.name=='nt' else 'clear')
            print(Fore.MAGENTA)
            draw_board()
            print(Fore.WHITE)
            if counter % 2 == 0:
                take_input(o)
            else:
                take_input(x)
            if counter > 3:
                victory = check_win()
                if victory:
                    print(Fore.GREEN)
                    draw_board()
                    if victory==check_win() and victory==o:
                        print(Fore.BLUE)
                        print(player_2, "победил(-а)!")
                        print(Fore.WHITE)
                        break
                    if victory==check_win() and victory==x:
                        print(Fore.BLUE)
                        print(player_1, "победил(-а)!")
                        print(Fore.WHITE)
                        break
            counter += 1
            if counter > 8:
                draw_board()
                print(Fore.YELLOW)
                print("Ничья!")
                print(Fore.WHITE)
                break
        

main()