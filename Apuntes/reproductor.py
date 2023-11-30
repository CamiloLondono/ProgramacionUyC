import os
import tkinter as tk
from tkinter import filedialog
import pygame
import random

class MusicPlayer:
    def __init__(self, master):
        self.master = master
        self.master.title("Reproductor de Música")

        self.music_folder = ""
        self.music_files = []
        self.current_music_index = 0
        self.paused_time = 0
        self.track_length = 0  # Variable para almacenar la longitud de la pista actual

        # Inicializar Pygame mixer
        pygame.mixer.init()

        # Etiqueta para mostrar el nombre de la canción actual
        self.lbl_current_music = tk.Label(self.master, text="", font=("Helvetica", 12))
        self.lbl_current_music.pack(pady=10)

        # Lista para mostrar las canciones
        self.listbox_songs = tk.Listbox(self.master, selectmode=tk.SINGLE, font=("Helvetica", 10))
        self.listbox_songs.pack(pady=10)

        # Botones
        self.btn_browse = tk.Button(self.master, text="Seleccionar Carpeta", command=self.browse_music_folder)
        self.btn_play = tk.Button(self.master, text="Reproducir", command=self.play_music)
        self.btn_pause = tk.Button(self.master, text="Pausar", command=self.pause_music)
        self.btn_stop = tk.Button(self.master, text="Detener", command=self.stop_music)
        self.btn_prev = tk.Button(self.master, text="Anterior", command=self.prev_music)
        self.btn_next = tk.Button(self.master, text="Siguiente", command=self.next_music)
        self.btn_forward = tk.Button(self.master, text="Adelantar 10s", command=self.forward_music)
        self.btn_rewind = tk.Button(self.master, text="Retroceder 10s", command=self.rewind_music)

        # Colocar los botones en la interfaz
        self.btn_browse.pack(side=tk.LEFT, padx=10)
        self.btn_prev.pack(side=tk.LEFT, padx=10)
        self.btn_play.pack(side=tk.LEFT, padx=10)
        self.btn_pause.pack(side=tk.LEFT, padx=10)
        self.btn_stop.pack(side=tk.LEFT, padx=10)
        self.btn_next.pack(side=tk.LEFT, padx=10)
        self.btn_forward.pack(side=tk.LEFT, padx=10)
        self.btn_rewind.pack(side=tk.LEFT, padx=10)

        # Ajustar el tamaño de la ventana
        self.master.geometry("600x400")

    def browse_music_folder(self):
        self.music_folder = filedialog.askdirectory()
        if not self.music_folder:
            return
        pygame.mixer.music.stop()
        self.current_music_index = 0
        self.music_files = [file for file in os.listdir(self.music_folder) if file.endswith((".mp3", ".wav"))]
        if not self.music_files:
            print("No se encontraron archivos de música en la carpeta.")
            return
        self.master.title("Reproductor de Música - " + self.music_folder)
        self.update_song_list()
        self.update_current_music_label()

    def update_song_list(self):
        self.listbox_songs.delete(0, tk.END)
        for song in self.music_files:
            self.listbox_songs.insert(tk.END, song)

    def play_music(self):
        if not self.music_folder or not self.music_files:
            return
        pygame.mixer.music.stop()
        self.current_music_index = self.listbox_songs.curselection()[0] if self.listbox_songs.curselection() else 0
        random_music = os.path.join(self.music_folder, self.music_files[self.current_music_index])
        pygame.mixer.music.load(random_music)
        pygame.mixer.music.play(start=self.paused_time)
        self.track_length = pygame.mixer.Sound(random_music).get_length()  # Obtener la longitud de la pista
        self.update_current_music_label()

    def pause_music(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
            self.paused_time = pygame.mixer.music.get_pos() // 1000
            self.update_current_music_label("Pausado: " + self.music_files[self.current_music_index])

    def stop_music(self):
        pygame.mixer.music.stop()
        self.paused_time = 0  # Restablecer el tiempo de reproducción al detener la música
        self.current_music_index = 0
        self.update_current_music_label()

    def prev_music(self):
        if not self.music_folder or not self.music_files:
            return
        self.current_music_index = (self.current_music_index - 1) % len(self.music_files)
        self.paused_time = 0  # Restablecer el tiempo de reproducción al cambiar de canción
        self.play_music()

    def next_music(self):
        if not self.music_folder or not self.music_files:
            return
        self.current_music_index = (self.current_music_index + 1) % len(self.music_files)
        self.paused_time = 0  # Restablecer el tiempo de reproducción al cambiar de canción
        self.play_music()

    def forward_music(self):
        if pygame.mixer.music.get_busy():
            current_time = pygame.mixer.music.get_pos() // 1000
            new_time = min(current_time + 10, self.track_length)  # Utilizar la longitud de la pista almacenada
            pygame.mixer.music.play(start=new_time)

    def rewind_music(self):
        if pygame.mixer.music.get_busy():
            current_time = pygame.mixer.music.get_pos() // 1000
            new_time = max(current_time - 10, 0)
            pygame.mixer.music.play(start=new_time)

    def update_current_music_label(self, text=None):
        if text is None and self.music_files:
            text = self.music_files[self.current_music_index]
        self.lbl_current_music.config(text=text)

if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayer(root)
    root.mainloop()
