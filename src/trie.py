class Trie:
    def __init__(self):

        self.isLeaf = False  # set when node is a leaf node
        self.character = {}


def insert(head: Trie, string: str):
    current = head

    for s in string:
        current = current.character.setdefault(s, Trie())

    current.isLeaf = True



def findLongestCommonSequence(head: Trie):
    sequence = ''
    current = head
    while not current.isLeaf and len(current.character) == 1:
        for k, v in current.character.items():
            sequence += k
            current = v
    return sequence


