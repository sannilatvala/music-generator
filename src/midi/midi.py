from pathlib import Path
import os
import mido


class MidiHandler:
    """
    A class for handling MIDI files.

    Attributes:
        input_midi_file (mido.MidiFile or None): The input MIDI file being processed.
    """

    def __init__(self):
        self.input_midi_file = None

    def parse_midi_file(self, midi_file):
        """
        Parses a MIDI file to extract note information.

        Args:
            midi_file (str): The filename of the MIDI file to parse.

        Returns:
            list: A list of notes extracted from the MIDI file.
        """

        notes = []
        try:
            # Get the directory of the current script file
            dirname = os.path.dirname(__file__)
            # Construct the full path of the MIDI file
            file_path = os.path.join(dirname, "..", "assets", midi_file)

            self.input_midi_file = mido.MidiFile(file_path, clip=True)

            for msg in self.input_midi_file:
                if msg.type == "note_on" and msg.velocity != 0:
                    # Only pick the notes that contain the melody
                    if msg.channel in [0, 10]:
                        notes.append(msg.note)

        except Exception as e:
            print(f"\nError parsing MIDI file: {e}")
        return notes

    def create_and_save_midi(self, generated_sequence, output_file):
        """
        Creates a MIDI file from a generated sequence of notes and saves it.

        Args:
            generated_sequence (list): A list of notes representing the generated sequence.
            output_file (str): The filename of the output MIDI file.

        Returns:
            str: The path to the saved MIDI file.
        """

        mid = mido.MidiFile()
        track = mido.MidiTrack()
        mid.tracks.append(track)
        start_msg = mido.Message(
            "program_change", channel=0, program=0, time=0)
        track.append(start_msg)
        track.append(mido.MetaMessage("set_tempo", tempo=mido.bpm2tempo(300)))

        for note in generated_sequence:
            track.append(mido.Message(
                "note_on", note=note, velocity=64, time=0))
            track.append(mido.Message(
                "note_off", note=note, velocity=64, time=700))

        generated_folder = Path("generatedfiles")
        generated_folder.mkdir(exist_ok=True)

        output_path = generated_folder.joinpath(output_file)

        mid.save(output_path)

        return output_path
