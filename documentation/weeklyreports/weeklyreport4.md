# Weekly report 4

This week I began with setting up a workflow for my project and creating a badge for the CI in my readme. I also transitioned my application to operate solely via the command line interface for simpicity. 

My focus has been on what happens after the user's choice of input MIDI file and the generation of the note sequence by the Markov chain. I also identified an issue with duplicate notes in the input sequence, which resulted in the markov chain malfunctioning. After resolving this issue, the note generation process now functions correctly.

Throughout the week, I encountered challenges while constructing the MIDI file, requiring time to determine the optimal method for adding notes to achieve a good sound quality. There are still areas for improvement with this.

To enhance user accessibility, I created a MIDI file for "Twinkle Twinkle Little Star" using Musescore. This serves as a convenient default option for users, sparing them the effort of creating their own MIDI files. Users now have the flexibility to choose between utilizing a MIDI file from the dataset or uploading their own. Users also have the option to download the generated MIDI file and use music software that supports midi files for playing the notes.

This week I invested approximately 20 hours into my project, primarily focusing on refining the user interface, as well as implementing functionalities for creating and dowloading the midi file from the generated notes. Additionally, I enhanced test coverage for markov_chain.py and trie.py.

In the upcoming week, my main priority will be to enhance the quality of my code by implementing necessary improvements and addressing minor issues. Additionally, I'll dedicate time to refining the documentation, particularly focusing on the testing and implementation documents. Moreover, I aim to increase test coverage significantly, striving for close to 100% coverage.