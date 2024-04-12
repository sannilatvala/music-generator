import unittest
from models.markov_chain import MarkovChain


class TestMarkovChain(unittest.TestCase):
    def setUp(self):
        self.notes = [44, 45, 47, 49, 50, 52, 54, 56, 54, 55]
        self.ngram = 1
        self.markov_chain = MarkovChain(self.notes, self.ngram)
        self.markov_chain.create_model()

    def test_create_model(self):
        unique_notes = list(set(self.notes[:-1]))
        root_children = self.markov_chain.trie.root.children

        self.assertTrue(all(note in root_children for note in unique_notes))

    def test_generate_sequence(self):
        length = 10
        generated_sequence = self.markov_chain.generate_sequence(length)

        self.assertEqual(len(generated_sequence), 10)
