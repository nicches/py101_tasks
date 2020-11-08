"""
Программа генерирует число от 0 до 1_000_000 и предлагает угадать его.

Программа должна приветствовать пользователя и считывать число с клавиатуры
Если число меньше загаданного, то программа выводит сообщение о том, что число
меньше
Если больше загаданного, то программа выводит сообщение о том, что больше

Программа должна выводить сообщения-предупреждения, если:
* пользователь ввёл не число
* число не входит в обозначенный в условии диапазон
Если пользователь ничего не ввёл/ввёл "exit", то происходит выход из программы.

Тебе может понадобится модуль random, цикл while и ветвления
"""

if __name__ == '__main__':
    pass

print ('Welcome! Please guess the number!')
import random
any_number = random.randint(1, 1000000)
while True:
    number = input(f'Please, guess the number: ')
    if number == "" or number == "exit":
        print("Wrong!")
        break
    if not number.isdigit():
        print(f"Please, insert the number")
        continue

    number = int(any_number)

    if number < 1 or number > 1000000:
        print(f"Number isn't in range")
        continue
    if number == any_number:
        print(f'You are Right!!!')
        break
 
 
    elif number < any_number:
        print(f'The number is bigger')
    else:
        print(f'The number is less')