
import random


# играющий сдаётся, если он вводит одно из этих слов
EXIT_WORDS = {"quit", "exit", "сдаюсь", "выход"}

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


def get_random_word(file_path):
    "Выбрать слово для игры."
    # TODO


def print_introduction():
    "Распечатать вводное сообщение."
    # TODO


def get_input(guessed_letters):
    "Получить инпут от юзера и проверить корректность."
    # TODO


def display_board(missed_letters, correct_letters, word):
    "Проверить букву в слове и вывести текущее состояние игры."
    # TODO


def play_again():
    "Спросить, продолжаем ли игру, и вернуть ответ. "
    # TODO


def main():
    "Общая логика работы."

    # TODO


if __name__ == "__main__":
    main()
