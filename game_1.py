import random

num = random.randint(1, 100)
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

while True:
    num_user = input("Введите число от 1 до 100: ")
    if not is_valid(num_user):
        print("А может быть все-таки введем целое число от 1 до 100?")
        continue
    if not 1 <= int(num_user) <= 100:
        print("А может быть все-таки введем целое число от 1 до 100?")
    else:
        if int(num_user) < num:
            print("Ваше число меньше загаданного, попробуйте еще разок")
        elif int(num_user) > num:
            print("Ваше число больше загаданного, попробуйте еще разок")
        else:
            print("Вы угадали, поздравляем!")
            print("Спасибо, что играли в числовую угадайку. Еще увидимся...")
            break
