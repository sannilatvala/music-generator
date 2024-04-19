import os
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
        self.input_sequence = None
        self.generated_sequence = None
        self.file_choice = None
        self.midi_file = None
        self.length = None
        self.ngram = None
        self.output_path = None

    def get_user_input(self):
        while True:
            choice = input(
                "\nDo you want to use your own midi file (Type 'O') or use one from the data (Type 'D')? ").strip().lower()
            
            if choice == "o":
                self.midi_file = input(
                    "\nPlease type the name of your MIDI file (make sure your file is in the 'assets' folder): ")

            elif choice == "d":
                self.get_file_choice()
                if self.file_choice == "1":
                    self.midi_file = "TwinkleTwinkleLittleStar.mid"
                    print(GREEN + "\nUsing TwinkleTwinkleLittleStar.mid from the data" + RESET)

                elif self.file_choice == "2":
                    self.midi_file = "FurElise.mid"
                    print(GREEN + "\nUsing FurElise.mid from the data" + RESET)

                elif self.file_choice == "3":
                    self.midi_file = "RiverFlowsInYou.mid"
                    print(GREEN + "\nUsing RiverFlowsInYou.mid from the data" + RESET)

            else:
                print(
                    RED + "\nInvalid choice. Please enter 'O' to use your own MIDI file or 'D' to use one from the data." + RESET)
                continue

            self.input_sequence = self.midi.parse_midi_file(
                self.midi_file)
            
            if self.input_sequence:
                break
        
            print(RED + "\nNo valid notes found in MIDI file." + RESET)

        self.get_desired_length()
        self.get_ngram_size()

    def get_file_choice(self):
        while True:
            file_choice = input(
                "\nWhich file do you want to use: \n"
                "\n(1) TwinkleTwinkleLittleStar.mid\n"
                "(2) FurElise.mid\n"
                "(3) RiverFlowsInYou.mid\n"
                "\nEnter your choice: "
            )
            if file_choice in ("1", "2", "3"):
                self.file_choice = file_choice
                break
            print(RED + "\nInvalid input. Please enter either 1, 2, or 3." + RESET)

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
        while True:
            try:
                self.ngram = int(input("\nDesired Markov Chain degree (recommended: 5-10): "))
                if self.ngram >= len(self.input_sequence):
                    print(RED + "\nThe length of the Markov Chain degree is too long compared to the number of input notes. Please choose a lower degree size." + RESET)
                    continue
                if self.ngram > 0:
                    break
                print(RED + "\nMarkov Chain degree must be a positive integer." + RESET)

            except ValueError:
                print(RED + "\nInvalid input. Please enter a valid integer." + RESET)

    def generate_music(self):
        markov_chain = MarkovChain(self.input_sequence, self.ngram)
        markov_chain.create_model()
        self.generated_sequence = markov_chain.generate_sequence(
            self.length)

    def start_ui(self):
        print(BOLD + "\nWelcome to the Markov Chain Music Generator!" + RESET)

        while True:
            user_input = input(
                "\nPlease choose one of the following options:\n"
                "\n(1) Upload a MIDI file and generate music\n"
                "(2) Save the generated music to MIDI\n"
                "(3) Play the generated music\n"
                "(0) Exit\n"
                "\nEnter your choice: "
            )

            if user_input not in ("0", "1", "2", "3"):
                print(RED + "\nInvalid input. Please enter either 0, 1, or 2." + RESET)
                continue

            if user_input == "0":
                break
            if user_input == "1":
                self.get_user_input()
                if self.midi_file is not None:
                    self.generate_music()
                    if self.generated_sequence:
                        print(
                            GREEN + "\nSequence of notes generated successfully. Now you can type 2 to download MIDI file" + RESET)

            if user_input == "2":
                if self.generated_sequence:
                    while True:
                        output_file = input("\nEnter the name of the output MIDI file (format: filename.mid or filename.midi): ")
                        if not output_file:
                            print(RED + "\nPlease provide a file name." + RESET)
                            continue

                        dirname = os.path.dirname(__file__)
                        
                        output_path = os.path.join(dirname, "..", "..", "generatedfiles", output_file)
                        
                        if not output_file.endswith(('.mid', '.midi')):
                            print(RED + "\nInvalid file format. Please use '.mid' or '.midi' extension." + RESET)
                            continue

                        if os.path.exists(output_path):
                            print(RED + f"\nFile '{output_file}' already exists. Please choose a different name." + RESET)
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
