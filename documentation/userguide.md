# User guide

## Instructions for starting the app

Begin by cloning the repository to your computer. You can do this by opening a terminal or command prompt and using the following command:

```bash
git clone <repository_url>
```

Navigate to the root directory of the project in your terminal or command prompt. You can use the 'cd' command to change directories:

```bash
cd <project_directory>
```

The app comes with a set of MIDI files located in the 'src/assets' folder, which you can use for generating music.

If you wish to use your own MIDI files, ensure they are in the correct format (filename.mid or filename.midi) and move them to the 'src/assets' folder within the project directory before starting the application.

Install the application dependencies with the following command:

```bash
poetry install
```

Start the application with the following command:

```bash
poetry run invoke start
```

## Other command line functions

Run tests with the following command:

```bash
poetry run invoke test
```

Create coverage report with the following command:

```bash
poetry run invoke coverage-report
```

Run pylint with the following command:

```bash
poetry run invoke lint
```

## Instructions for using the application

When you start the application, you'll be greeted with the following interface:

![image](https://github.com/sannilatvala/music-generator/assets/119106675/767aaa4a-8226-4595-8ae9-4a210302cd5d)

You can select any of the given 5 options by typing the corresponding number and pressing enter. To proceed with options 2, 3, and 4, you'll need to upload your preferred MIDI files first by entering the number 1.

After entering the number 1, you'll be greeted with the following:

![image](https://github.com/sannilatvala/music-generator/assets/119106675/a6fa189c-af5c-43c6-be62-9ec8d75caf93)

The available MIDI files will update based on the contents of the assets folder.

You have the option to either select all files by typing 'all' or specify individual files by entering their corresponding numbers separated by commas. For example, to choose files 1, 2, and 3, you would input '1,2,3' and press enter.

After selecting the files, you'll be prompted to specify the desired length of the generated sequence. While the recommended range is 50-100, you can choose a longer sequence, keeping in mind that it cannot exceed 1000 notes.

![image](https://github.com/sannilatvala/music-generator/assets/119106675/8756adbe-ab8e-4e16-81ef-f5c38116b9e6)

Next, you'll be prompted to specify the desired Markov chain degree. It's recommended to choose a degree between 2 and 5. Note that selecting longer Markov chain degrees requires a substantial amount of data. Otherwise, there's a risk that the generated sequence of notes may closely resemble one of the original songs in the dataset.

![image](https://github.com/sannilatvala/music-generator/assets/119106675/3d205959-d912-49a4-bec2-05c035773984)

Once you've finished specifying all the parameters for generating the sequence of notes, you can proceed by entering the number 2 to save the notes to a MIDI file. Simply provide the desired output file name when prompted. The output file will be saved to the 'generatedfiles' folder within the project directory.

![image](https://github.com/sannilatvala/music-generator/assets/119106675/8e42bad2-2bc3-4360-9d19-1bc8800cbc64)

You can now open the MIDI file using your preferred program or type 3 on the command line to play the music.

![image](https://github.com/sannilatvala/music-generator/assets/119106675/84472228-b83c-452d-9ebc-ab4faa029798)

To show the generated sequence of notes you can type 4.

![image](https://github.com/sannilatvala/music-generator/assets/119106675/ae733681-64b5-4029-be90-c2ef44a9ebfc)



