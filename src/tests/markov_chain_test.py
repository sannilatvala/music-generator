import unittest
from models.markov_chain import MarkovChain


class TestMarkovChain(unittest.TestCase):
    def setUp(self):
        self.notes = ['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C']
        self.markov_chain = MarkovChain(self.notes)
        self.markov_chain.create_model()

    def test_trie_initialization(self):
        self.assertTrue(self.markov_chain.trie.root.children)

    def test_trie_population(self):
        unique_notes = self.markov_chain.unique_notes
        root_children = self.markov_chain.trie.root.children

        self.assertTrue(all(note in root_children for note in unique_notes))

    def test_generate_sequence(self):
        generated_sequence = self.markov_chain.generate_sequence(length=10)

        self.assertEqual(10, len(generated_sequence))
