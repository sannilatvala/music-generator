class TrieNode:
    def __init__(self, note=None):
        self.note = note
        self.children = {}
        self.transition_counts = 0
        self.end_of_sequence = False

class Trie:
    """
    A trie data structure for storing and retrieving data
    """

    def __init__(self):
        self.root = TrieNode()

    def insert_notes(self, notes):

        current_node = self.root

        for note in notes:
            if note not in current_node.children:
                current_node.children[note] = TrieNode(note)

            current_node = current_node.children[note]
            current_node.transition_counts += 1

        current_node.end_of_sequence = True
