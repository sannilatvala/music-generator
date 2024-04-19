import os
from ansicodes import RED, RESET

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

class MidiPlayer:
    def __init__(self):
        pygame.mixer.init()

    def play_midi_file(self, midi_file):
        try:
            pygame.mixer.music.load(midi_file)
            pygame.mixer.music.play()
            print("\nPress Ctrl + C to interrupt playback.")
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(50)
        except KeyboardInterrupt:
            print(RED + "\nPlayback interrupted by user." + RESET)
            pygame.mixer.music.stop()
