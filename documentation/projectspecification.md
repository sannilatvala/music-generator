# Project specification

## Project overview

The purpose of this project is to develop a music generator using the Markov Chain algorithm and a trie data structure for efficient sequence storage. The generator will analyze musical input data, such as chords or notes, to predict the following state based on the recent one. This prediction will happen by identifying transition probabilities learned from the training data.

## Algorithms and data structures

The **Markov Chain** algorithm will be used for predicting the probability of a sequence occurrence based on recent musical events.

A **Trie data structure** will be used for storing and retrieving musical sequences efficiently.

## Problem being solved

The main goal of this project is to generate music sequences that follow a specific style or genre, based on the provided training data.

## Program inputs and usage

### Input data

Markov Chain degree: Users specify the degree of the Markov Chain, which determines the order of sequence prediction. This can be provided as a numerical value, such as 1 for first order and 2 for second order.

Musical input data: Users provide musical input data, such as MIDI-files or text representations of notes or chords, to train the Markov Chain algorithm. 

Output Length: Users specify the desired length of the generated music sequence. This is represented as a numerical value indicating the number of notes or time steps in the sequence.

### Usage

Users can execute the program by providing musical input data and parameters via command-line arguments. The program then generates music sequences according to the specified parameters and user preferences.

## Programming language for the project

The programming language that is used for developing this project is python. Additionally, I have some experience in JavaScript allowing me to peer review projects implemented in JavaScript if needed.

## Language of the project documentation

English will be used for both the program code and documentation.

## Desired time and space complexities

**Degree 1 Markov chain**

Time Complexity: The time complexity is O(KN)

Space Complexity: The space complexity is O(KN)

**Degree 2 Markov chain**

Time Complexity: The time complexity is O(K²N)

Space Complexity: The space complexity is O(KN)

K = number of states, N = number of time steps

## Study program

The study program I am enrolled in is the Bachelor of Computer Science (CS).

## References

References will be added to the implementation document as the project progresses.