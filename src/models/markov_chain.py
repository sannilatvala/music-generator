import random
from models.trie import Trie


class MarkovChain:
    """
    A Markov chain model for music generation.

    Attributes:
        sequences (list): A list of sequences used to train the Markov chain.
        ngram (int): The size of the Markov chain degree used for prediction.
        trie (Trie): A Trie data structure used for storing transition probabilities.
    """

    def __init__(self, sequences, ngram):
        self.sequences = sequences
        self.ngram = ngram
        self.trie = Trie()

    def create_model(self):
        """
        Creates the Markov chain model by inserting sequences into the Trie.
        """

        for sequence in self.sequences:
            for i in range(len(sequence)-self.ngram):
                notes = sequence[i:i+self.ngram+1]
                self.trie.insert_notes(notes)

    def get_next_note(self, notes):
        """
        Retrieves the next note based on the given sequence of notes.

        Args:
            notes (list): The sequence of notes.

        Returns:
            int or None: The next note to be added to the sequence, or None if the sequence is not found.
        """

        current_sequence = notes

        if self.trie.search_sequence(current_sequence):
            next_notes = self.trie.get_next_notes(current_sequence)
            if next_notes:
                return random.choices(list(next_notes.keys()), weights=list(next_notes.values()))[0]

        return None

    def generate_sequence(self, length):
        """
        Generates a sequence of notes using the Markov chain model.

        Args:
            length (int): The desired length of the generated sequence.

        Returns:
            list: A list of notes representing the generated sequence.
        """

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
