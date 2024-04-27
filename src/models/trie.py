class TrieNode:
    def __init__(self, note=None):
        self.note = note
        self.children = {}
        self.transition_counts = 0
        self.end_of_sequence = False


class Trie:
    """
    A trie data structure for storing data
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

    def search_sequence(self, sequence):
        current_node = self.root
        for note in sequence:
            if note not in current_node.children:
                return False
            current_node = current_node.children[note]

        return True

    def get_next_notes(self, sequence):
        """
        Retrieves the possible next notes and their transition counts
        given a specific sequence of notes.

        Args:
            sequence: The sequence of notes.

        Returns:
            A dictionary where keys are the possible next notes and values
            are their corresponding transition counts.
        """

        current_node = self.root

        # Traverse the Trie using the given sequence
        for note in sequence:
            if note not in current_node.children:
                return {}  # Return an empty dictionary if the sequence does not exist
            current_node = current_node.children[note]

        # Retrieve the possible next notes and their transition counts from the current node's children
        next_notes = {
            child.note: child.transition_counts for child in current_node.children.values()}
        return next_notes
