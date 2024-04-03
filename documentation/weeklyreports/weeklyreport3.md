# Weekly report 3

This week I began with addressing issues encountered in the Markov chain algorithm. The sequence insertion into the trie tree was incorrect, leading to inaccuracies in the calculated weights or "transition counts". Additionally, several minor errors were detected and resolved. As a result of these fixes, the algorithm now functions correctly, making it possible to start implementing new features.

The initial focus was on crafting a user interface using Streamlit, chosen for its enhanced convenience compared to the command line. Through the Streamlit app, users can input either a sequence of notes separated by spaces or upload a MIDI file. 

Right now, there are no functionalities for downloading a MIDI file from the generated sequence of notes, however, this will be addressed in the upcoming week. Upon pressing the "generate" button, the current implementation solely produces a list of notes based on the provided input, utilizing the Markov chain algorithm and trie data structure.

This week I also installed necessary dependencies for my project and created the file tasks.py to define project tasks. Additionally, I enhanced test coverage.

I found that this week presented fewer challenges with the project compared to last week. Once I got the algorithm functioning properly, the project progressed without major difficulties. However, I did encounter some challenges with the MIDI file and Streamlit components, primarily due to my lack of prior experience with them.

This week, I invested approximately 11 hours into my project, primarily focusing on coding and less time dedicated to research. I created the midi.py file to manage file upload functionalities and generate notes from the provided data. Additionally, I created app.py to initialize the application and improved ui.py to enhance its capability in managing user interface functionalities.

Next week I will focus on what happens after the user clicks the button "generate" Specifically, the focus will be on creating a downloadable MIDI file from the generated sequence and exploring options for playing the music generated from the notes.