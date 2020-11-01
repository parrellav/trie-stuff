class Trie2:
    def __init__(self):

        self.isLeaf = False
        self.character = {}

def insert_ord(head: Trie2, string: str):
    current = head

    for s in string:
        current = current.character.setdefault(ord(s)-ord('a'), Trie2())

    current.isLeaf = True

def sort_lex(head: Trie2, my_string: str):
    if head.isLeaf:
        print(my_string)
    for x in range(26):
        if x in head.character:
            sort_lex(head.character[x], my_string + chr(x + ord('a')))
