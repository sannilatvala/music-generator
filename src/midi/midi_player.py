import os
from ansicodes import RED, RESET

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "true"
import pygame


class MidiPlayer:
    """
    A class for playing MIDI files.
    """

    def __init__(self):
        pygame.mixer.init()

    def play_midi_file(self, midi_file):
        """
        Plays a MIDI file.

        Args:
            midi_file (str): The filepath of the MIDI file to play.

        Raises:
            KeyboardInterrupt: If playback is interrupted by the user.
        """

        try:
            pygame.mixer.music.load(midi_file)
            pygame.mixer.music.play()
            print("\nPress Ctrl + C to interrupt playback.")
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(50)
        except KeyboardInterrupt:
            print(RED + "\nPlayback interrupted by user." + RESET)
            pygame.mixer.music.stop()
        except Exception as e:
            raise RuntimeError(f"Error playing MIDI file: {e}") from e
