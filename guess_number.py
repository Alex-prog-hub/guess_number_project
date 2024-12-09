

from random import randint
number = randint(1,100)
print('Угадайте число от 1 до 100')

while True:
    guess = int(input('Введите число:'))
     # Если число меньше загаданного...
    if guess < number:
        # ...выводим сообщение.
        print('Ваше число меньше того, что загадано.')
    elif guess > number:
        # ...выводим сообщение.
        print('Ваше число больше того, что загадано.')
    elif guess == number:
        # ...прерываем выполнение программы и...
        break
print('Отличная интуиция! Вы угадали число :)')