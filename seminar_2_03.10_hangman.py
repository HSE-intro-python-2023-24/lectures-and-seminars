
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


def get_input(guessed_letters):
    "Получить инпут от юзера и проверить корректность. + стоп слова"    
    not_correct = True
    while not_correct:
        letter = input('Введи букву: ')
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
        else:
            not_correct = False
            return letter
            

def display_board(missed_letters, correct_letters, word):
    "Проверить букву в слове и вывести текущее состояние игры."
    # TODO


def play_again():
    "Спросить, продолжаем ли игру, и вернуть ответ. "
    # TODO


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

    # Сюда складываем буквы, которые пользователь угадал
    guessed_letters = []
    letter = get_input(guessed_letters)


if __name__ == "__main__":
    main()
