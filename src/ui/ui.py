import streamlit as st
from models.markov_chain import MarkovChain
from midi.midi import MidiHandler


class UserInterface:
    """
    A user inteface for handling user input and output
    """

    def __init__(self):
        self.midi = MidiHandler()

    def get_user_input(self):
        notes = st.text_input("Input sequence of notes separated by spaces:")
        midi_file = st.file_uploader("Upload MIDI file", type=['mid', 'midi'])
        length = st.number_input(
            "Length of the generated music sequence:", min_value=1, step=1)
        return notes, midi_file, length

    def generate_music(self, notes, length):
        input_sequence = notes.split()
        markov_chain = MarkovChain(input_sequence)
        markov_chain.create_model()
        generated_sequence = markov_chain.generate_sequence(length)
        return generated_sequence

    def display_generated_sequence(self, generated_sequence):
        st.write("Generated sequence:", generated_sequence)

    def start_ui(self):
        st.title("Music Generator")

        notes, midi_file, length = self.get_user_input()

        if st.button("Generate"):
            if notes:
                generated_sequence = self.generate_music(notes, length)
                self.display_generated_sequence(generated_sequence)
            elif midi_file is not None:
                generated_sequence = self.midi.generate_music_from_midi(
                    midi_file, length)
                self.display_generated_sequence(generated_sequence)
            else:
                st.error(
                    "Please provide input sequence of notes or upload a MIDI file.")
