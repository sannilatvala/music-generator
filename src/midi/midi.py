from pathlib import Path
import os
import mido


class MidiHandler:
    def __init__(self):
        self.input_midi_file = None

    def parse_midi_file(self, midi_file):
        notes = []
        try:
            # Get the directory of the current script file
            dirname = os.path.dirname(__file__)
            # Construct the full path of the MIDI file
            file_path = os.path.join(dirname, "..", "assets", midi_file)

            self.input_midi_file = mido.MidiFile(file_path, clip=True)

            for msg in self.input_midi_file:
                if msg.type == "note_on" and msg.velocity != 0:
                    notes.append(msg.note)

        except Exception as e:
            print(f"\nError parsing MIDI file: {e}")
        return notes

    def create_and_save_midi(self, generated_sequence, output_file):
        mid = mido.MidiFile()
        track = mido.MidiTrack()
        mid.tracks.append(track)
        track.append(mido.MetaMessage("set_tempo", tempo=mido.bpm2tempo(300)))

        for note in generated_sequence:
            track.append(mido.Message(
                "note_on", note=note, velocity=64, time=100))
            track.append(mido.Message(
                "note_off", note=note, velocity=64, time=700))

        generated_folder = Path("generatedfiles")
        generated_folder.mkdir(exist_ok=True)

        output_path = generated_folder.joinpath(output_file)

        mid.save(output_path)

        return output_path
