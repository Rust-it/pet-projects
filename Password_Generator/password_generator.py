import string
from random import choice

# Функции для проверки ввода
def check_positive_integer(input_str):
    """Проверяет, является ли строка положительным целым числом."""
    return input_str.isdigit() and int(input_str) > 0

def check_yes_no(input_str):
    """Проверяет, является ли ответ 'да' или 'нет'."""
    return input_str.strip().lower() in ["да", "нет"]

# Функция для запроса параметров у пользователя
def get_user_input(prompt, validation_func):
    """Получает ввод от пользователя с заданной проверкой."""
    while True:
        user_input = input(prompt).strip()
        if validation_func(user_input):
            return user_input
        print("Некорректный ввод. Попробуйте снова.")

# Сбор всех параметров
number_passwords = int(get_user_input("Какое количество паролей нужно для генерации? (целое число): ", check_positive_integer))
len_password = int(get_user_input("Какая длина одного пароля? (целое число): ", check_positive_integer))

# Начальный набор символов (используем строки из модуля string)
chars = ""
if get_user_input("Включать ли цифры 0123456789? (да/нет): ", check_yes_no) == "да":
    chars += string.digits
if get_user_input("Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (да/нет): ", check_yes_no) == "да":
    chars += string.ascii_uppercase
if get_user_input("Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (да/нет): ", check_yes_no) == "да":
    chars += string.ascii_lowercase
if get_user_input("Включать ли символы !#$%&*+-=?@^_? (да/нет): ", check_yes_no) == "да":
    chars += string.punctuation

# Исключение неоднозначных символов
if get_user_input("Исключать ли неоднозначные символы il1Lo0O? (да/нет): ", check_yes_no) == "да":
    ambiguous_chars = "il1Lo0O"
    chars = ''.join(c for c in chars if c not in ambiguous_chars)

# Функция для генерации пароля
def generate_password(length, chars):
    """Генерирует случайный пароль заданной длины из допустимых символов."""
    return ''.join(choice(chars) for _ in range(length))

# Генерация и вывод паролей
for _ in range(number_passwords):
    print(generate_password(len_password, chars))
