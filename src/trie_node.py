class TrieNode:

    def __init__(self, char=''):
        self.childern = [None] * 26 # letters in US alphabet
        self.is_end_word = False
        self.char = char

    def set_is_end_word(self, a_end_word):
        self.is_end_word = a_end_word

    def get_is_end_word(self):
        return self.is_end_word