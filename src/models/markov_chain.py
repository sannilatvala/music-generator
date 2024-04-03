import random
from models.trie import Trie


class MarkovChain:
    """
    A markov chain model for music generation
    """

    def __init__(self, notes):
        self.unique_notes = list(set(notes))
        self.notes = notes
        self.trie = Trie()

    def create_model(self, ngram=1):
        for i in range(len(self.notes)-ngram):
            sequence = self.notes[i:i+ngram+1]
            self.trie.insert_notes(sequence)

    def generate_sequence(self, length):
        current_node = random.choice(list(self.trie.root.children.values()))
        sequence = [current_node.note]

        for _ in range(length - 1):
            if current_node.end_of_sequence:
                # if current node is not a child of the root (i.e, it is the last note of the
                # sequence without chilren) choose a random node from the children of the root
                if current_node.note in self.trie.root.children:
                    current_node = self.trie.root.children[current_node.note]
                else:
                    current_node = random.choice(
                        list(self.trie.root.children.values()))
                    sequence.append(current_node.note)
                    continue

            transition_counts = [
                node.transition_counts for node in current_node.children.values()]

            next_node = random.choices(
                list(current_node.children.values()),
                weights=transition_counts
            )[0]

            sequence.append(next_node.note)
            current_node = next_node
        return sequence
