import random
def password_generation():
    digits = '0123456789'
    lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
    uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    punctuation = '!#$%&*+-=?@^_'



    password_lenth = int(input(f"Введите длинну пароля : "))
    dit = input(f"Включать ли цифры ? 'ДА' или 'НЕТ': ").upper()
    u_c_l = input(f"Включать ли прописные буквы ? 'ДА' или 'НЕТ': ").upper()
    l_c_l = input(f"Включать ли строчные буквы ? 'ДА' или 'НЕТ': ").upper()
    punc = input(f"Включать ли спецсимволы '!#$%&*+-=?@^_'  ? 'ДА' или 'НЕТ': ").upper()

    dif_pass = []
    if dit == 'ДА':
        dif_pass.extend(digits)
    if u_c_l == 'ДА':
        dif_pass.extend(uppercase_letters)
    if l_c_l =='ДА':
        dif_pass.extend(lowercase_letters)
    if punc == 'ДА':
        dif_pass.extend(punctuation)
    random.shuffle(dif_pass)

    your_password = []

    for j in range(password_lenth):
        your_password.append(random.choice(dif_pass))
    r = ''.join(your_password)
    return r + ''

print(password_generation())
