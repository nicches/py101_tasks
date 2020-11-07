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
entered_number = input('Please, guess the number: ')

while entered_number != ( '','exit' ) :
    if entered_number == "" or entered_number == "exit":
        print("Wrong")
        break

    if not entered_number.isdigit():
        print("Please, insert the number")
        continue

    try entered_number = int(entered_number)

    if entered_number < 1 or entered_number > 1000000:
        print("Number isn't in range")
        continue

    if entered_number == any_number:
        print('You are Right!!!')
        break
 
    elif entered_number < any_number:
        print('The number is greater')
    else:
        print('The number is less')

entered_number = input('Please, guess the number: ')