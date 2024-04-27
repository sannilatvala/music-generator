import os
import midi
from models.markov_chain import MarkovChain
from midi.midi import MidiHandler
from midi.midi_player import MidiPlayer
from ansicodes import RED, GREEN, RESET, BOLD


class UserInterface:
    """
    A user inteface for handling user input and output
    """

    def __init__(self):
        self.midi = MidiHandler()
        self.player = MidiPlayer()
        self.input_sequences = []
        self.file_choices = []
        self.generated_sequence = []
        self.file_choice = None
        self.midi_file = None
        self.length = None
        self.ngram = None
        self.output_path = None

    def get_user_input(self):
        while True:
            choice = input(
                "\nDo you want to use your own MIDI files (Type 'O') or use ones from the data (Type 'D')? ").strip().lower()

            if choice == "o":
                while True:
                    midi_file = input(
                        "\nPlease type the name of your MIDI file (make sure your file is in the 'assets' folder), or type 'done' to finish: ").strip()

                    if midi_file.lower() == "done":
                        break

                    dirname = os.path.dirname(__file__)
                    file_path = os.path.join(dirname, "..", "assets", midi_file)
                    if not os.path.exists(file_path):
                        print(
                            RED + "\nThe specified MIDI file does not exist in the 'assets' folder." + RESET)
                        continue

                    if midi_file in self.file_choices:
                        print(RED + f"\nMIDI file {midi_file} already added" + RESET)
                        continue
                    
                    else:
                        self.file_choices.append(midi_file)
                        self.input_sequences.append(
                            self.midi.parse_midi_file(midi_file))
                    
                        print(GREEN + f"\n{midi_file} added" + RESET)

            elif choice == "d":
                self.get_file_choices()
                print(
                    GREEN + "\nUsing the following MIDI files from the data:\n" + RESET)
                for midi_file in self.file_choices:
                    print(f"- {midi_file}")
                    self.input_sequences.append(
                        self.midi.parse_midi_file(midi_file))

            else:
                print(
                    RED + "\nInvalid choice. Please enter 'O' to use your own MIDI files or 'D' to use ones from the data." + RESET)
                continue

            if self.input_sequences:
                break

            print(RED + "\nNo valid notes found in any MIDI file." + RESET)

        self.get_desired_length()
        self.get_ngram_size()

    def get_file_choices(self):
        dirname = os.path.dirname(__file__)
        assets_path = os.path.join(dirname, "..", "assets")
        midi_files = sorted(os.listdir(assets_path))

        # Check if there are MIDI files in the assets directory
        if not midi_files:
            print(RED + "\nNo MIDI files found in the assets directory." + RESET)
            return

        while True:
            print("\nAvailable MIDI files:\n")
            for i, file_name in enumerate(midi_files, start=1):
                print(f"({i}) {file_name}")

            choice = input(
                "\nEnter the numbers of the MIDI files you want to use separated by commas (or type 'all' to choose all files): ").strip()

            if choice.lower() == "all":
                self.file_choices.extend(midi_files)
                break

            # Validate if input consists of valid integers separated by commas
            if all(index.isdigit() for index in choice.split(",")):
                file_indices = [int(index) - 1 for index in choice.split(",")]
                valid_indices = all(0 <= idx < len(midi_files)
                                    for idx in file_indices)
                if valid_indices:
                    selected_files = [midi_files[file_index]
                                      for file_index in file_indices]
                    self.file_choices.extend(selected_files)
                    break
                else:
                    print(
                        RED + "\nInvalid choice. Please enter numbers within the range." + RESET)
            else:
                print(
                    RED + "\nInvalid input. Please enter valid integers separated by commas or type 'all' to choose all files" + RESET)

    def get_desired_length(self):
        while True:
            try:
                self.length = int(
                    input("\nDesired length of the generated music sequence (recommended: 50-100): "))
                if self.length > 0:
                    break
                print(RED + "\nLength must be a positive integer." + RESET)

            except ValueError:
                print(RED + "\nInvalid input. Please enter a valid integer." + RESET)

    def get_ngram_size(self):
        total_note_length = sum((len(sequence)
                                for sequence in self.input_sequences))
        while True:
            try:
                self.ngram = int(
                    input("\nDesired Markov Chain degree (recommended: 2-5): "))
                if self.ngram > 0:
                    if self.ngram <= total_note_length:
                        break
                    else:
                        print(
                            RED + "\nThe Markov Chain degree exceeds the total length of notes in the MIDI files. Please choose a smaller degree." + RESET)
                else:
                    print(
                        RED + "\nMarkov Chain degree must be a positive integer." + RESET)

            except ValueError:
                print(RED + "\nInvalid input. Please enter a valid integer." + RESET)

    def generate_music(self):
        markov_chain = MarkovChain(self.input_sequences, self.ngram)
        markov_chain.create_model()
        self.generated_sequence = markov_chain.generate_sequence(self.length)

    def start_ui(self):
        print(BOLD + "\nWelcome to the Markov Chain Music Generator!" + RESET)

        while True:
            user_input = input(
                "\nPlease choose one of the following options:\n"
                "\n(1) Upload a MIDI file and generate music\n"
                "(2) Save the generated music to MIDI\n"
                "(3) Play the generated music\n"
                "(4) Show the generated sequence\n"
                "(0) Exit\n"
                "\nEnter your choice: "
            )

            if user_input not in ("0", "1", "2", "3", "4"):
                print(
                    RED + "\nInvalid input. Please enter a number between 0 and 4." + RESET)
                continue

            if user_input == "0":
                break

            if user_input == "1":
                self.input_sequences = []
                self.file_choices = []
                self.get_user_input()
                if self.input_sequences:
                    self.generate_music()
                    if self.generated_sequence:
                        print(
                            GREEN + "\nSequence of notes generated successfully. Now you can type 2 to download MIDI file" + RESET)
                    else:
                        print(
                            RED + "\nFailed to generate notes. The specified length or degree may be too long for the available input data." + RESET)

            if user_input == "2":
                if self.generated_sequence:
                    while True:
                        output_file = input(
                            "\nEnter the name of the output MIDI file (format: filename.mid or filename.midi): ")
                        if not output_file:
                            print(RED + "\nPlease provide a file name." + RESET)
                            continue

                        dirname = os.path.dirname(__file__)

                        output_path = os.path.join(
                            dirname, "..", "..", "generatedfiles", output_file)

                        if not output_file.endswith(('.mid', '.midi')):
                            print(
                                RED + "\nInvalid file format. Please use '.mid' or '.midi' extension." + RESET)
                            continue

                        if os.path.exists(output_path):
                            print(
                                RED + f"\nFile '{output_file}' already exists. Please choose a different name." + RESET)
                            continue

                        self.output_path = self.midi.create_and_save_midi(
                            self.generated_sequence, output_file)
                        print(
                            GREEN + "\nMIDI file saved to 'generatedfiles' folder" + RESET)
                        print(
                            GREEN + "\nNow you can type 3 to play the generated music or use a software or devices that support MIDI files" + RESET)
                        break

                else:
                    print(RED + "\nPlease generate music before saving" + RESET)
                    continue

            if user_input == "3":
                if self.output_path:
                    self.player.play_midi_file(self.output_path)
                else:
                    print(RED + "\nPlease save generated music before playing" + RESET)

            if user_input == "4":
                if self.generated_sequence:
                    print("\nGenerated Sequence:")
                    print("\n", self.generated_sequence)
                else:
                    print(
                        RED + "\nPlease generate music before showing the sequence" + RESET)
