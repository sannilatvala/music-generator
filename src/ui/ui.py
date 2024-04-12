from models.markov_chain import MarkovChain
from midi.midi import MidiHandler
from ansicolors import RED, GREEN, RESET


class UserInterface:
    """
    A user inteface for handling user input and output
    """

    def __init__(self):
        self.midi = MidiHandler()
        self.generated_sequence = None
        self.midi_file = None
        self.length = None
        self.ngram = None

    def get_user_input(self):
        while True:
            choice = input(
                "\nDo you want to use your own midi file (Type 'O') or use one from the data (Type 'D')? ").strip().lower()
            
            if choice == "o":
                self.midi_file = input(
                    "\nPlease type the name of your MIDI file (make sure your file is in the 'midi' folder): ")
                break

            elif choice == "d":
                self.midi_file = "TwinkleTwinkleLittleStar.mid"
                print(GREEN + "\nUsing TwinkleTwinkleLittleStar.mid from the data" + RESET)
                break
            else:
                print(
                    RED + "\nInvalid choice. Please enter 'O' to use your own MIDI file or 'D' to use one from the data." + RESET)
                self.get_user_input()

        while True:
            try:
                self.length = int(
                    input("\nDesired length of the generated music sequence (recommended: 20-50): "))
                if self.length > 0:
                    break
                print(RED + "\nLength must be a positive integer." + RESET)

            except ValueError:
                print(RED + "\nInvalid input. Please enter a valid integer." + RESET)

        while True:
            try:
                self.ngram = int(input("\nPlease enter the desired ngram size (recommended: 2-5): "))
                if self.ngram > 0:
                    break
                print(RED + "\nNgram size must be a positive integer." + RESET)

            except ValueError:
                print(RED + "\nInvalid input. Please enter a valid integer." + RESET)

    def generate_music(self):
        input_sequence = self.midi.parse_midi_file(
            self.midi_file)
        if input_sequence:
            markov_chain = MarkovChain(input_sequence, self.ngram)
            markov_chain.create_model()
            self.generated_sequence = markov_chain.generate_sequence(
                self.length)
        else:
            print(RED + "\nNo valid notes found in MIDI file." + RESET)

    def start_ui(self):
        print("Music Generator")

        while True:
            user_input = input(
                "\nType 1 to upload midi file and generate music, 2 to save generated music to MIDI, and 0 to exit: ")

            if user_input not in ("0", "1", "2"):
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
                    output_file = input(
                        "\nEnter the name of the output MIDI file: ")
                    self.midi.create_and_save_midi(
                        self.generated_sequence, output_file)
                    print(
                        GREEN + "\nMIDI file saved to 'generatedfiles' folder" + RESET)
                    print(
                        GREEN + "\nNow you can play the notes using software or devices that support MIDI files" + RESET)
                else:
                    print(RED + "\nPlease generate music before saving" + RESET)
                    continue
