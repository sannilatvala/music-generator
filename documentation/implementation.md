# Implementation document

## Introduction

The purpose of this Music Generator project is to give users tools for generating music sequences using the Markov Chain algorithm and a trie data structure. This document provides an overview of the project's implementation details, including the general structure of the program, algorithms, data structures, time and space complexities, references, and other relevant information.

## Structure of the project

The structure of the project is divided into several components:

### Root Directory

- README.md: A markdown file providing an overview of the project and links to documentation files.
- tasks.py: Task automation file containing commands for project management tasks, such as running tests, formatting code, and running the program.
- pyproject.toml: Configuration file for project settings and dependencies managed by Poetry.
- documentation: Directory containing project documentation files.
- generatedfiles: Directory to store generated MIDI files.

### Source Code Directory (src):

- User Interfac (ui.py): Handles user input and output, providing a command-line interface for interacting with the Music Generator.

- Models:
    - Markov Chain (markov_chain.py): Module implementing the Markov Chain algorithm for music generation.
    - Trie (trie.py): Module defining the trie data structure for efficient sequence storage.

- MIDI Handling:
    - Midi handler (midi.py): Module handling MIDI file parsing and MIDI file creation.
    - MIDI Player (midi_player.py): Module for playing MIDI files using the pygame library.

- Assets:
    - Folder containing sample MIDI files and other input data used for training the model.

### Tests Directory (tests):

- test_markov_chain.py: Unit tests for the Markov Chain algorithm implementation.
- test_trie.py: Unit tests for the trie data structure implementation.
- test_midi.py: Unit tests for MIDI file parsing and MIDI file creation.

## Algorithms and Data Structures

### Markov Chain Algorithm:

- Utilized for predicting the probability of a note occurrence based on recent musical events.
- Implemented to generate music sequences that follow a specific style or genre.

### Trie Data Structure:

- Used for efficient storage of musical sequences.
- Enhances the performance of the Markov Chain algorithm by efficiently managing transition probabilities.

## Time and Space Complexities

- Trie data structure: 
    - The time complexity for a trie data structure is O(W*L), where W is the number of notes and L is the average length of each sequence.
    - The space complexity for a trie data structure is O(N*k), where N is the number of nodes in the trie and k is the number of unique notes.

- Markov Chain: The time complexity for the generate_sequence() method in the Markov Chain class is O(n*m). Where n is the desired length of the generated sequence and m is the number of attempts made. In the worst case, where the loop runs for 100 attempts without finding a valid sequence, m would be 100.

## Potential Shortcomings

- MIDI file handling: The quality of the music and the MIDI file handling could be improved. To do this it's essential to invest time in developing algorithms to accurately identify the melody channel within MIDI files. While the application performs well with simple songs primarily composed of piano music, refining the channel selection process can further enhance its performance across a broader range of musical compositions.

- User Input Handling: The user interface class relies on command-line input, which might not provide the most user-friendly experience. Adding a graphical user interface or web interface could enhance usability.

## Potential Improvements

- Enhance error handling mechanisms and provide more informative error messages.

- Improving the quality of the code.

- Adding more comments to clarify logic.


## Use of Extensive Language Models

I have used ChatGPT to explain me parts of how the algorithms I used works, as I've noticed that ChatGPT is good at explaining the logic behind code. In addition, whenever I've had trouble with errors in my code that I couldn't quite figure out, I've asked ChatGPT to pinpoint the issue and suggest ways to fix it.

## References

- Midi files obtained from freemidi.org: https://freemidi.org/

    - RiverFlowsInYou.mid: https://freemidi.org/download3-15836-river-flows-in-you-yiruma
    - FurElise.mid: https://freemidi.org/download3-26718-fur-elise-artists-bands

- Midi files obtained from bitmidi.com: https://bitmidi.com/

    - BeethovenMoonlightSonata.mid: https://bitmidi.com/beethoven-moonlight-sonata-mid
    - Nocturne.mid: https://bitmidi.com/nocturne-in-e-flat-opus-9-nr-2-mid
    - UneComptineD'unAutre.mid: https://bitmidi.com/yann-tiersen-une-comptine-dun-autre-mid