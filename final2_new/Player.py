class Player:
    def __init__(self, name, user_word):
        self.name = name
        self.user_words = user_word
        self.count = 0
        self.user_input = []

    def print_name(self):
        print(f"Привет, {self.name}")

    def count_words(self, user_list):
        self.user_input = user_list
        self.count = len(self.user_input)
        print(f"Игра завершена , вы угадали {self.count} слов!")
