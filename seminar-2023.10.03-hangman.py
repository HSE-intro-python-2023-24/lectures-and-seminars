
import random


# играющий сдаётся, если он вводит одно из этих слов
EXIT_WORDS = ["quit", "exit", "сдаюсь", "выход"]

HANGMAN_PICS =  ['''
     +---+
         |
         |
         |
        ===''', '''
     +---+
     O  |
        |
        |
       ===''', '''
    +---+
    O   |
    |   |
        |
       ===''', '''
    +---+
    O   |
   /|   |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
   /    |
       ===''', '''
    +---+
    O   |
   /|\  |
   / \  |
       ===''']


def get_random_word(file_path='./resources/hangman_words.txt'): 
    "Выбрать слово для игры."
    with open(file_path, encoding='utf-8') as f:
        words = f.readlines()
    
    clean_words = []
    
    for w in words:
        clean_words.append(w.strip('\n').lower())
    
    word = random.choice(clean_words)
    
    return word
    

def print_introduction():
    "Распечатать вводное сообщение."
    print("Добро в виселицу! Угадай слово или умри! \nУ тебя есть 7 попыток, чтобы угадать слово.")
    print("Если надоело играть, введи одно из стоп слов: {}".format(','.join(EXIT_WORDS)))


def get_input(guessed_letters, missed_letters):
    "Получить инпут от юзера и проверить корректность. + стоп слова"    
    not_correct = True
    while not_correct:
        letter = input('Введи букву: ').lower()
        if not letter.isalpha():
            print('Надо ввести именно букву или стоп-слово!')
            continue
        elif len(letter) > 1:
            if letter in EXIT_WORDS:
                print('Как жаль, что ты уходишь :\'(')
                break
            else:
                print('Надо ввести только одну букву!')
                continue
        elif (letter in guessed_letters) or (letter in missed_letters):
            print('Вы уже вводили эту букву и она верная. Введите другую: ')
            continue
        else:
            not_correct = False
            return letter
            

def is_in_word(word_list, letter, guessed_letters, missed_letters):
    "Проверить букву в слове."
    if letter in word_list:
        guessed_letters.append(letter)
    else:
        missed_letters.append(letter)


def display_board(missed_letters, guessed_letters, word):
    "Вывести текущее состояние игры."
    num_letters = len(word)
    word_string = ['_'] * num_letters
    for lt_1 in guessed_letters:
        if lt_1 in word:
            idx = []
            for i, lt_2 in enumerate(word): 
                if lt_2 == lt_1:
                    word_string[i] = lt_1
    
    print(HANGMAN_PICS[len(missed_letters)])
    current_string = ' '.join(word_string)
    print(current_string)
    print('Уже введенные неправильные буквы: ', ', '.join(missed_letters))
    print('Осталось {} попыток\n\n'.format(6 - len(missed_letters)))


def play_again():
    "Спросить, продолжаем ли игру, и вернуть ответ. "
    # TODO
    return input('Если хочешь начать новую игру, напиши "да": ')

def main():
    "Общая логика работы."
    # TODO
    # Печатаем приветствие 
    # Загадали слово
    # Получаем букву у пользователя + проверить корректность 
    # Проверяем, есть буква в слове + печатаем борд
    # Проверка на выиграл / проиграл
    # Спросить, хочет ли еще
    
    print_introduction()
    word = get_random_word()
    word_list = list(word)

    # Сюда складываем буквы, которые пользователь угадал
    guessed_letters = []
    missed_letters = []
    
    while True:
    
        letter = get_input(guessed_letters, missed_letters)
        is_in_word(word_list, letter, guessed_letters, missed_letters)
        display_board(missed_letters, guessed_letters, word)
        
        word_list = [w for w in word_list if w not in guessed_letters]
        
        if len(missed_letters) > 5: 
            print('Ты проиграл')
            print('Загаданное слово: {}\n'.format(word))
            answer = play_again()
            if answer == 'да':
                print('Поехали!\n')
                word = get_random_word()
                word_list = list(word)
                guessed_letters = []
                missed_letters = []
            else:
                break
        if len(word_list) == 0:
            print('Ты выиграл\n')
            answer = play_again()
            if answer == 'да':
                print('Поехали!\n')
                word = get_random_word()
                word_list = list(word)
                guessed_letters = []
                missed_letters = []
            else:
                break
            

if __name__ == "__main__":
    main()

