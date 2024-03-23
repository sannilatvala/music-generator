from models.trie import Trie
import random

class MarkovChain:
    """
    A markov chain model for music generation
    """

    def __init__(self, notes):
        self.unique_notes = list(set(notes))
        self.notes = notes
        self.trie = Trie()

    def train(self):
        for i in range(len(self.notes)):
            sequence = self.notes[i:]
            self.trie.insert_notes(sequence)

    def generate_sequence(self, length):
        current_node = random.choice(list(self.trie.root.children.values()))
        sequence = [current_node.note]

        for _ in range(length - 1):
            if current_node.end_of_sequence:
                current_node = self.trie.root.children[current_node.note]

            transition_counts = [node.transition_counts for node in current_node.children.values()]

            print(transition_counts)

            next_node = random.choices(
                list(current_node.children.values()),
                weights=transition_counts
            )[0]

            sequence.append(next_node.note)
            current_node = next_node
        return sequence
