class Wordcounter:

    def __init__(self, sentence):
        self.sentence = sentence
        self.word = self.count_words()

    def count_words(self):
        return self.sentence.split()

    def get_word_count(self):
        return len(self.word)

    def get_shortest_word(self):
        letters = len(self.word[0].split())

        for word in self.word:
            if len(word) < letters:
                letters = len(word)
        return letters

    def get_longest_word(self):
        letters = 0

        for word in self.word:
            if len(word) > letters:
                letters = len(word)
        return letters
