encryption_or_decryption = input('Шифрование или дешифрование? Введите "ш" или "д" : ')
language = input('Русский или английский? Введите "р" или "а" :')
k = int(input('Шаг сдвига (со сдвигом вправо)?'))
alphabet_RU = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
alphabet_ru = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
alphabet_EN = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabet_en = 'abcdefghijklmnopqrstuvwxyz'
s = input('Введите строку')
s1 = ''
if encryption_or_decryption.lower() == 'ш':
    if language.lower() == 'р':
        for c in s:
            if c in alphabet_RU:
                s1 += alphabet_RU[(alphabet_RU.find(c) + k) % 32]
            elif c in alphabet_ru:
                s1 += alphabet_ru[(alphabet_ru.find(c) + k) % 32]
            else:
                s1 += c
    elif language.lower() == 'а':
        for c in s:
            if c in alphabet_EN:
                s1 += alphabet_EN[(alphabet_EN.find(c) + k) % 26]
            elif c in alphabet_en:
                s1 += alphabet_en[(alphabet_en.find(c) + k) % 26]
            else:
                s1 += c
if encryption_or_decryption.lower() == 'д':
    if language.lower() == 'р':
        for c in s:
            if c in alphabet_RU:
                s1 += alphabet_RU[(alphabet_RU.find(c) - k) % 32]
            elif c in alphabet_ru:
                s1 += alphabet_ru[(alphabet_ru.find(c) - k) % 32]
            else:
                s1 += c
    elif language.lower() == 'а':
        for c in s:
            if c in alphabet_EN:
                s1 += alphabet_EN[(alphabet_EN.find(c) - k) % 26]
            elif c in alphabet_en:
                s1 += alphabet_en[(alphabet_en.find(c) - k) % 26]
            else:
                s1 += c
print(s1)