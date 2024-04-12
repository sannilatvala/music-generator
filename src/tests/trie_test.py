import unittest
from models.trie import Trie

class TestTrie(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()
        self.notes = [44, 45, 47, 49, 50, 52, 54, 56]
        self.ngram = 1

    def test_transition_counts(self):

        for i in range(len(self.notes)-self.ngram):
            sequence = self.notes[i:i+self.ngram+1]
            self.trie.insert_notes(sequence)

        node = self.trie.root

        for child_node in node.children.values():
            self.assertEqual(child_node.transition_counts, 1)

    def test_end_of_sequence(self):

        for i in range(len(self.notes)-self.ngram):
            sequence = self.notes[i:i+self.ngram+1]
            self.trie.insert_notes(sequence)

        node = self.trie.root

        for child_node in node.children.values():
            for child in child_node.children.values():
                self.assertTrue(child.end_of_sequence)
