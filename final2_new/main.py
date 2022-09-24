
"""''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
                                MAIN
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''"""


from utils import *
import time

if __name__ == '__main__':
    name = input("Ввведите имя игрока: \n") # input the player game
    new_word, sub_new = random_word()  # creating a random word
    word1 = BasicWord(new_word, sub_new)  # creating an object BasicWord
    player1 = Player(name, sub_new)  # creating an object Player
    player1.print_name()  # printig the user name
    print("Слова должны быть не короче 3 букв")
    print("Чтобы закончить игру, угадайте все слова или напишите stop")
    time.sleep(2)
    print(repr(word1))  # printing a random word
    time.sleep(2)
    user_words = check_word(sub_new)  # list of words that user ques
    player1.count_words(user_words)  # counting and printing the amount of wright words
