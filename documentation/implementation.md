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
    - Directory containing sample MIDI files or other input data used for training the model.

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

## Potential Shortcomings and Improvements

## Use of Extensive Language Models

## References

- Midi files obtained from freemidi.org: https://freemidi.org/

    - RiverFlowsInYou.mid: https://freemidi.org/download3-15836-river-flows-in-you-yiruma
    - FurElise.mid: https://freemidi.org/download3-26718-fur-elise-artists-bands
