from models.markov_chain import MarkovChain
from ui import get_user_input


def main():
    notes, length = get_user_input()

    input_sequence = notes.split()

    markov_chain = MarkovChain(input_sequence)
    markov_chain.train()
    generated_sequence = markov_chain.generate_sequence(length)

    print(generated_sequence)

if __name__ == "__main__":
    main()
