import random

word_list = [
    "человек", "слово", "лицо", "дверь", "земля", "работа", "ребенок",
    "история", "женщина", "развитие", "власть", "правительство", "начальник",
    "спектакль", "автомобиль", "экономика", "литература", "граница", "магазин",
    "председатель", "сотрудник", "республика", "личность"
]

def get_word():
    """Возвращает случайное слово из списка, преобразованное в верхний регистр."""
    return random.choice(word_list).upper()

def display_hangman(tries):
    """Возвращает изображение виселицы в зависимости от количества оставшихся попыток."""
    stages = [
        ''' 
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           - 
        ''',
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           - 
        ''',
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           - 
        ''',
        '''
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           - 
        ''',
        '''
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           - 
        ''',
        '''
           --------
           |      |
           |      O
           |    
           |      
           |     
           - 
        ''',
        '''
           --------
           |      |
           |      
           |    
           |      
           |     
           - 
        '''
    ]
    return stages[tries]

def play(word):
    """Основная логика игры."""
    tries = 6
    word_completion = ['_'] * len(word)
    guessed_letters = set()
    guessed_words = set()

    print('Давайте играть в угадайку слов!')
    print(display_hangman(tries))
    print(' '.join(word_completion))
    print()

    while tries > 0:
        guess = input('Введите букву или слово целиком: ').upper()

        if len(guess) == 1 and guess.isalpha():  # Проверка на букву
            if guess in guessed_letters:
                print(f'Вы уже называли букву "{guess}".')
            elif guess not in word:
                print(f'Буквы "{guess}" нет в слове.')
                tries -= 1
                guessed_letters.add(guess)
            else:
                print(f'Отлично, буква "{guess}" есть в слове!')
                guessed_letters.add(guess)
                word_completion = [
                    guess if word[i] == guess else word_completion[i]
                    for i in range(len(word))
                ]
                if '_' not in word_completion:
                    print('Поздравляем, вы угадали слово! Вы победили!')
                    break
        elif len(guess) == len(word) and guess.isalpha():  # Проверка на слово
            if guess in guessed_words:
                print(f'Вы уже называли слово "{guess}".')
            elif guess != word:
                print(f'Слово "{guess}" неверное.')
                tries -= 1
                guessed_words.add(guess)
            else:
                print('Поздравляем, вы угадали слово! Вы победили!')
                break
        else:
            print('Введите одну букву или целое слово.')
        
        print(display_hangman(tries))
        print(' '.join(word_completion))
        print()

    if tries == 0:
        print(f'Вы не угадали слово. Загаданным словом было "{word}".')

def main():
    """Основная функция для повторных игр."""
    while True:
        word = get_word()
        play(word)
        again = input('Играем еще раз? (да или нет): ').lower()

        # Проверяем правильный ввод (только "да" или "нет")
        while again not in ['да', 'нет']:
            again = input('Пожалуйста, введите "да" или "нет": ').lower()

        if again == 'нет':
            print('Спасибо за игру! До свидания!')
            break

if __name__ == '__main__':
    main()
