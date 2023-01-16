from colorama import*
init()

def greet():
    print("______________________")
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT + "   Приветствуем Вас   ")
    print(Style.BRIGHT + "в игре Крестики-нолики")
    print("______________________")
    print(Style.BRIGHT + "    Формат ввода: x y ")
    print(Style.BRIGHT + "x - номер строки, y - номер столбца" + Style.RESET_ALL)

def show():
    print()
    print(f"    | 0 | 1 | 2 |")
    print("  _______________")
    for i, row in enumerate(field):
        row_str = f"  {i} | {' | '.join(row)} |"
        print(row_str)
        print("  _______________")
    print()

def question():
    while True:
        version = input(          "Введите координаты: ").split()

        if len (version) != 2:
            print("Введите 2 координаты через пробел!")
            continue

        x,y = version

        if not(x.isdigit()) or not(y.isdigit()):
            print("Введите числа через пробел!")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print("Неверные координаты, попробуйте еще раз!")
            continue

        if field[x][y] != " ":
            print("Клетка занята, попробуйте еще раз!")
            continue

        return x, y

def check_win():
    win_raffle = (
    ((0, 0), (0, 1), (0, 2)),
    ((1, 0), (1, 1), (1, 2)),
    ((2, 0), (2, 1), (2, 2)),
    ((0, 0), (1, 0), (2, 0)),
    ((0, 1), (1, 1), (2, 1)),
    ((0, 2), (1, 2), (2, 2)),
    ((0, 0), (1, 1), (2, 2)),
    ((0, 2), (1, 1), (2, 0))
)
    for cord in win_raffle:
        symbols = []
        for a in cord:
            symbols.append(field[a[0]][a[1]])
        if symbols == ["Ϫ", "Ϫ", "Ϫ"]:
            print(Fore.LIGHTRED_EX + "Победил Ϫ!" + Style.RESET_ALL)
            return True
        if symbols == ["Ω", "Ω", "Ω"]:
            print(Fore.LIGHTRED_EX + "Победил Ω!" +  Style.RESET_ALL)
            return True
    return False

greet()
field = [[" "] * 3 for i in range(3) ]
motion = 0

while True:
    motion += 1
    show()
    if motion % 2 == 1:
        print(Fore.CYAN + "Ходит крестик" +  Style.RESET_ALL)
    else:
        print(Fore.GREEN + "Ходит нолик" +  Style.RESET_ALL)

    x,y = question()

    if motion % 2 == 1:
        field [x][y] = "Ϫ"
    else:
        field [x][y] = "Ω"

    if check_win():
        break

    if motion == 9:
        print("Ходы закончились! Ничья!")
        break
