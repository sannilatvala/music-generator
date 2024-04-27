import unittest
from models.trie import Trie


class TestTrie(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()
        self.notes = [44, 45, 47, 49, 50, 52, 54, 56]
        self.ngram = 1
        self.insert_sequence(self.notes)

    def insert_sequence(self, sequence):
        for i in range(len(sequence) - self.ngram):
            notes_to_insert = sequence[i:i+self.ngram+1]
            self.trie.insert_notes(notes_to_insert)

    def test_transition_counts(self):
        node = self.trie.root

        for child_node in node.children.values():
            self.assertEqual(child_node.transition_counts, 1)

    def test_end_of_sequence(self):
        node = self.trie.root

        for child_node in node.children.values():
            for child in child_node.children.values():
                self.assertTrue(child.end_of_sequence)
