import unittest
import os
import mido
from midi.midi import MidiHandler


class TestMidiHandler(unittest.TestCase):
    """
    Unit tests for the MidiHandler class.
    """

    def setUp(self):
        self.midi_handler = MidiHandler()

    def test_parsing_valid_midi_file(self):
        """
        Test parsing a valid MIDI file.
        """

        midi_file = "FurElise.mid"
        notes = self.midi_handler.parse_midi_file(midi_file)

        self.assertTrue(isinstance(notes, list))
        self.assertTrue(all(isinstance(note, int) for note in notes))

    def test_parsing_invalid_midi_file(self):
        """
        Test parsing an invalid MIDI file.
        """

        invalid_midi_file = "invalid.mid"
        with self.assertRaises(FileNotFoundError):
            self.midi_handler.parse_midi_file(invalid_midi_file)

    def test_create_and_save_midi(self):
        """
        Test creating and saving a MIDI file.
        """

        generated_sequence = [44, 45, 47, 49, 50, 52, 54, 56]
        output_file = "output.mid"
        output_path = self.midi_handler.create_and_save_midi(
            generated_sequence, output_file)
        self.assertTrue(output_path.exists())
        output_path.unlink()
