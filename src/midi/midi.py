import mido
import streamlit as st
from models.markov_chain import MarkovChain
import os


class MidiHandler:

    def parse_midi_file(self, midi_file):
        notes = []
        try:
            # Get the directory of the current script file
            dirname = os.path.dirname(__file__)
            # Construct the full path of the MIDI file
            file_path = os.path.join(dirname, midi_file.name)

            with open(file_path, "wb") as file:
                file.write(midi_file.getbuffer())
            midi_file = mido.MidiFile(file_path)
            for msg in midi_file:
                if msg.type == "note_on":
                    notes.append(msg.note)

        except Exception as e:
            st.error(f"Error parsing MIDI file: {e}")
        finally:
            # Delete the temporary file
            os.unlink(file_path)
        return notes

    def generate_music_from_midi(self, midi_file_path, length):
        input_sequence = self.parse_midi_file(midi_file_path)
        if input_sequence:
            markov_chain = MarkovChain(input_sequence)
            markov_chain.create_model()
            generated_sequence = markov_chain.generate_sequence(length)
            return generated_sequence
        else:
            st.error("No valid notes found in MIDI file.")
