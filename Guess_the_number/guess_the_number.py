import random

print("Добро пожаловать в числовую угадайку!")

print("До какого числа будете угадывать?")
while True:
    right = input("Укажите число от 2 до ∞: ")
    if right.isdigit():
        right = int(right)
        if right > 1:
            hidden = random.randint(1, right)
            break
        else:
            continue
    else:
        print("Некорректный ввод.")


def is_valid(s):
    return s.isdigit() and 1 <= int(s) <= right


count = 0
while True:
    num = input("Введите число: ")
    count += 1
    if is_valid(num) == False:
        print(f"А может быть все-таки введем целое число от 1 до {right}")

    num = int(num)

    if num < hidden:
        print("Ваше число меньше загаданного, попробуйте еще разок")
    elif num > hidden:
        print("Ваше число больше загаданного, попробуйте еще разок")
    else:
        print(f"Вы угадали за {count} попыток, поздравляем!")
        if input("Сыграть снова - да, любой ввод - нет: ") == "да":
            count = 0
            right = int(input("Укажите число от 2 до ∞: "))
            hidden = random.randint(1, right)
            continue
        else:
            break

print("Спасибо, что играли в числовую угадайку. Еще увидимся...")
