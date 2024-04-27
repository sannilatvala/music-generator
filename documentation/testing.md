# Testing document

## What has been tested and how?

#### MarkovChain:

- test_create_model: This test ensures that the Markov chain model is created correctly by checking if all unique notes in the input sequences are present as children of the root node in the trie.

- test_generate_sequence: Verifies that the generated sequence has the specified length.

- test_generated_note_chains_in_original_notes: Checks if the generated sequence consists of note chains (length = ngram+1) is present in the original sequences. This ensures that the markov chain agorithm and trie data structure works correctly.

#### MidiHandler:

- test_parsing_valid_midi_file: Checks if the MIDI file is parsed correctly, ensuring that the output is a list of integers representing notes.

- test_parsing_invalid_midi_file: Verifies that an invalid MIDI file results in an empty list.

- test_create_and_save_midi: Tests the creation and saving of a MIDI file based on a generated sequence.

#### Trie:

- test_transition_counts: Checks if transition counts are correctly incremented when inserting sequences into the trie.

- test_end_of_sequence: Verifies that end-of-sequence flags are correctly set for nodes representing the end of a sequence.

## Inputs Used for Testing:

#### MarkovChain:

- Input sequences containing lists of integers representing musical notes.
- Parameters for n-gram size and desired sequence length.

#### MidiHandler:
- MIDI files for testing both valid and invalid inputs.

- Generated sequence of notes for creating and saving a MIDI file.


#### Trie:
- Sequences of musical notes for testing trie insertion.

- Parameter for the n-gram size.

## How to run the tests:

Run tests with the following command:

```bash
poetry run invoke test
```

Create coverage report with the following command:

```bash
poetry run invoke coverage-report
```

## Coverage Report: