class BasicWord:
    def __init__(self, basic_word, sub_word):
        self.basic_word = basic_word
        self.sub_word = sub_word
        self.word = ''
        self.sub_word_count = 0

    def __repr__(self):
        return f"Составьте {len(self.sub_word)} слов  из слова  {self.basic_word} \n " \
            #  f"{self.sub_word}" #for developer\checker



    def sub_word_cnt(self, sub_word):
        self.sub_word = sub_word
        self.sub_word_count = len(self.sub_word)
        return self.sub_word_count
