import pygame
from pynput import keyboard
import time

class oP1UM:
    def __init__(self):
        self.playlist = ["Playboi Carti – Stop Breathing.mp3", "Playboi Carti – Rockstar Made.mp3", "Playboi Carti – Sky.mp3"]
        self.cur_index = 0
        self.is_playing = False
        self.paused_time = 0
        self.paused = False

        pygame.mixer.init()

    def play_song(self):
        if not self.is_playing:
            if self.paused:
                pygame.mixer.music.unpause()
                print("Resuming:", self.playlist[self.cur_index], "from", self.paused_time, "seconds")
            else:
                pygame.mixer.music.load(self.playlist[self.cur_index])
                pygame.mixer.music.play()
                print("Playing:", self.playlist[self.cur_index])
            self.is_playing = True
            self.paused = False

    def stop_song(self):
        if self.is_playing:
            pygame.mixer.music.stop()
            print("Stopping:", self.playlist[self.cur_index])
            self.is_playing = False
            self.paused = False

    def pause_song(self):
        if self.is_playing and not self.paused:
            self.paused_time = pygame.mixer.music.get_pos() / 1000
            pygame.mixer.music.pause()
            print("Pausing:", self.playlist[self.cur_index], "at", self.paused_time, "seconds")
            self.paused = True

    def resume_song(self):
        if self.is_playing and self.paused:
            pygame.mixer.music.unpause()
            print("Resuming:", self.playlist[self.cur_index], "from", self.paused_time, "seconds")
            self.paused = False

    def next_song(self):
        self.stop_song()
        self.cur_index = (self.cur_index + 1) % len(self.playlist)
        self.play_song()

    def prev_song(self):
        self.stop_song()
        self.cur_index = (self.cur_index - 1) % len(self.playlist)  # Fixed typo here
        self.play_song()

def main():
    player = oP1UM()

    def on_press(key):
        try:
            if key.char == 'p': player.play_song()
            elif key.char == 's': player.stop_song()
            elif key.char == ' ': player.pause_song()
            elif key.char == 'r': player.resume_song()
            elif key.char == 'n': player.next_song()
            elif key.char == 'b': player.prev_song()
            elif key.char == 'q': 
                pygame.mixer.quit()
                return False  # Stop listener
        except AttributeError:
            pass

    print("Press 'p' to play, 's' to stop, 'space' to pause, 'r' to resume, 'n' for next song, 'b' for previous song, 'q' to quit ")

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()
