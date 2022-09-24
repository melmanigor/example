"""''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
                                functions
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''"""

from BasicWord import *
from Player import *
import requests  # request libary
import random

"""''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
        function that produse random word from json key
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''"""


def random_word():
    response = requests.get("https://api.jsonbin.it/bins/3wGuN95p")
    data = response.json()
    words = []  # list of keys
    sub_new = []  # list of values
    for i in data:
        words.append(i["word"])  # making a list from keys of json file
    random_word = random.choice(words)  # choosing random key we prpared on the list
    # print(random_word)
    for v in data:
        if random_word == v["word"]:
            sub_new = v["subwords"]  # making list of values of random key
    return random_word, sub_new


"""''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
        checking the input word fom user and add to a list
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''"""


def check_word(sub_new_word):
    use_words = []  # list that will contain all user words
    cnt = 0  # count the wright words of the user
    while cnt < len(sub_new_word):  # check the user word for all requers until it be equal to words is possible
        word = input(f"ваше {cnt + 1} слово: \n")  # user input word
        if word in sub_new_word and len(word) >= 3 and word not in use_words:  # all requerments
            cnt = cnt + 1  # words count
            use_words.append(word)  # making a list of good words
        elif len(word) < 3:  # short input word
            print("слишком короткое слово")
        elif word in use_words:  # already enterd by user
            print("уже использовано")
        elif word != "stop":
            print("неверно")  # the word that user enter dosnt match to the value in the list that come from random word
        # print(use_words) #for developer\checker
        # print(len(use_words))#for developer\checker
        if cnt == len(sub_new_word) or word == "stop":  # stop game condition
            return use_words
