import unittest
from models.markov_chain import MarkovChain


class TestMarkovChain(unittest.TestCase):
    """
    Unit tests for the MarkovChain class.

    Attributes:
        sequences (list): A list of sequences containing notes used for testing.
        ngram (int): The size of the Markov chain degree.
        length (int): The length of the generated sequence.
        markov_chain (MarkovChain): An instance of the MarkovChain class.
        generated_sequence (list): The generated sequence of notes.
    """

    def setUp(self):
        self.sequences = [[76, 75, 76, 75, 76, 71, 74, 72, 69, 45, 52, 57, 60,
                           64, 69, 40, 71, 52, 56, 64, 68, 71, 45, 72, 52, 57,
                           64, 76, 75, 76, 75, 76, 71, 74, 72, 69, 45, 52, 57,
                           60, 64, 69, 40, 71, 52, 56, 64, 72, 71, 45, 69, 52,
                           57, 64, 76, 75, 76, 75, 76, 71, 74, 72, 69, 45, 52,
                           57, 60, 64, 69, 40, 71, 52, 56, 64, 68, 71, 45, 72,
                           52, 57, 64, 76, 75, 76, 75, 76, 71, 74, 72, 69, 45,
                           52, 57, 60, 64, 69, 40, 71, 52, 56, 64, 72, 71, 45,
                           69, 52, 57, 71, 72, 74, 76, 48, 55, 60, 67, 77, 76,
                           43, 74, 55, 59, 65, 76, 74, 72, 45, 52, 57, 64, 74,
                           72, 40, 71, 52, 64, 64, 76, 64, 76, 76, 84, 75, 76,
                           75, 76, 75, 76, 75, 76, 75, 76, 75, 76, 71, 74, 72,
                           69, 45, 52, 57, 60, 64, 69, 40, 71, 52, 56, 64, 68,
                           71, 45, 72, 52, 57, 64, 76, 75, 76, 75, 76, 71, 74,
                           72, 69, 45, 52, 57, 60, 64, 69, 40, 71, 52, 56, 64,
                           72, 71, 33, 45, 69]]
        self.ngram = 3
        self.length = 100
        self.markov_chain = MarkovChain(self.sequences, self.ngram)
        self.markov_chain.create_model()
        self.generated_sequence = self.markov_chain.generate_sequence(
            self.length)

    def test_create_model(self):
        """
        Test whether the Markov chain model is created correctly.
        """

        unique_notes = list(set(self.sequences[:-self.ngram]))
        root_children = self.markov_chain.trie.root.children

        self.assertTrue(all(note in root_children for note in unique_notes))

    def test_generate_sequence(self):
        """
        Test that the generated sequence of notes has the correct length.
        """

        if self.generated_sequence:
            self.assertEqual(len(self.generated_sequence), self.length)

    def test_generate_sequence_returns_empty_list(self):
        """
        Test that generate_sequence method returns an empty list when no valid sequences can be generated.
        """

        sequences = [[1]]
        markov_chain = MarkovChain(sequences, self.ngram)
        markov_chain.create_model()
        generated_sequence = markov_chain.generate_sequence(
            self.length)
        
        self.assertEqual(generated_sequence, [])

    def test_generated_note_chains_in_original_notes(self):
        """
        Test if generated note chains are in the original sequences of notes.
        """

        if self.generated_sequence:
            chains = self.get_note_chains(self.sequences[0], self.ngram)

            for i in range(len(self.generated_sequence) - self.ngram):
                chain = self.generated_sequence[i:i+self.ngram+1]
                self.assertIn(chain, chains)

    def get_note_chains(self, notes, ngram):
        """
        Generate note chains from a list of notes.

        Args:
            notes (list): The list of notes.
            ngram (int): The size of the n-gram.

        Returns:
            list: A list of note chains.
        """

        chains = []
        for i in range(len(notes) - ngram):
            chain = notes[i:i+ngram+1]
            chains.append(chain)
        return chains
