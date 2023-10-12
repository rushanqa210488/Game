import random

print("Добро пожаловать в числовую угадайку")

def is_valid(numb):
    count_sym = 0
    for i in numb:
        if i in "0123456789":
            count_sym += 1
    if count_sym == len(numb):
        return True
    else:
        return False

def number_guessing_game():
    numb_bord = int(input())
    num = random.randint(1, numb_bord)
    counter = 0
    while True:
        counter += 1
        num_user = input(f"Введите число от 1 до {numb_bord}: ")
        if not is_valid(num_user):
            print(f"А может быть все-таки введем целое число от 1 до {numb_bord}?")
            continue
        if not 1 <= int(num_user) <= numb_bord:
            print(f"А может быть все-таки введем целое число от 1 до {numb_bord}?")
        else:
            if int(num_user) < num:
                print("Ваше число меньше загаданного, попробуйте еще разок")
            elif int(num_user) > num:
                print("Ваше число больше загаданного, попробуйте еще разок")
            else:
                print("Вы угадали, поздравляем!" f"C {counter} попыток")
                break

number_guessing_game()

one_more_time = input("Сыграем еще раз? Введите 'ДА' или 'НЕТ': ").upper()
if one_more_time == 'ДА':
    print("OK")
    number_guessing_game()
else:
    print("Спасибо, что играли в числовую угадайку. Еще увидимся...")
