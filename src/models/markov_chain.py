from operator import ne
import random
from models.trie import Trie


class MarkovChain:
    """
    A markov chain model for music generation
    """

    def __init__(self, sequences, ngram):
        self.sequences = sequences
        self.ngram = ngram
        self.trie = Trie()

    def create_model(self):
        for sequence in self.sequences:
            for i in range(len(sequence)-self.ngram):
                notes = sequence[i:i+self.ngram+1]
                self.trie.insert_notes(notes)

    def get_next_note(self, notes):
        current_sequence = notes

        if self.trie.search_sequence(current_sequence):
            next_notes = self.trie.get_next_notes(current_sequence)
            return random.choices(list(next_notes.keys()), weights=list(next_notes.values()))[0]

        return None

    def generate_sequence(self, length):

        attempts = 0
        while attempts < 100:
            start = random.choice(self.sequences[0])
            sequence = [start]

            # Construct the initial sequence based on the trie
            while len(sequence) < self.ngram:
                next_note = self.get_next_note(sequence)
                sequence.append(next_note)

            for _ in range(length - self.ngram):
                next_note = self.get_next_note(sequence[-self.ngram:])
                if next_note is None:
                    break
                sequence.append(next_note)

            if len(sequence) == length:
                return sequence

            attempts += 1

        # If the loop completes without generating a valid sequence, return an empty list
        return []
