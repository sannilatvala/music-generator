class TrieNode:
    """
    Represents a node in a Trie data structure.

    Attributes:
        note (int): The note associated with the node.
        children (dict): A dictionary containing a node and its children.
        transition_counts (int): The number of transitions from a node to its children.
        end_of_sequence (bool): Indicates if the node marks the end of a sequence.
    """

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
        """
        Initializes the Trie with an empty root node.
        """

        self.root = TrieNode()

    def insert_notes(self, notes):
        """
        Inserts a sequence of notes into the Trie.

        Args:
            notes (list): The list of notes to insert.
        """

        current_node = self.root

        for note in notes:
            if note not in current_node.children:
                current_node.children[note] = TrieNode(note)

            current_node = current_node.children[note]
            current_node.transition_counts += 1

        current_node.end_of_sequence = True

    def search_sequence(self, sequence):
        """
        Checks if a sequence of notes exists in the Trie.

        Args:
            sequence (list): The sequence of notes to search.

        Returns:
            bool: True if the sequence exists in the Trie, False otherwise.
        """

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
            sequence (list): The sequence of notes.

        Returns:
            Dictionary: A dictionary where keys are the possible next notes and values
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
