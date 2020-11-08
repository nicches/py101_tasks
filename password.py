import re
while True:
    password = input('Enter password: ')
    if len(password) >= 8 and re.search(r"[A-Z]", password) and re.search(r"[0-9]", password):
        print ( f'Password is hard' )
        break
    else:
        print ( f'Password is simple' )
pass

"""
Программа оценивает сложность пароля.

Пользователь вводит пароль, в ответ получает оценку "сложный"/"простой"
Сложным считается пароль, состоящий как минимум из 8-ми символов,
включая цифры и алфавитные символы
"""

if __name__ == '__main__':
    pass
