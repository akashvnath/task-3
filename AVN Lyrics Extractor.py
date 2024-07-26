import tkinter as tk
from tkinter import messagebox
import lyricsgenius

# Initialize Genius API
genius = lyricsgenius.Genius("2NP3iFVaB57J06ZDWB95eKFOpr4S5RHiHsl2k4lF7wlBPWkYRSBHan881bDME-B7")

def get_lyrics():
    song_title = song_title_entry.get()
    artist_name = artist_name_entry.get()

    if not song_title:
        messagebox.showerror("Input Error", "Song title is required.")
        return

    try:
        if artist_name:
            song = genius.search_song(song_title, artist_name)
        else:
            song = genius.search_song(song_title)
        
        if song:
            show_lyrics(song)
        else:
            messagebox.showinfo("Lyrics Not Found", "Lyrics not found. Please check the title and try again.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def show_lyrics(song):
    lyrics_window = tk.Toplevel(root)
    lyrics_window.title(f"Lyrics for '{song.title}' by {song.artist}")
    
    lyrics_text = tk.Text(lyrics_window, wrap=tk.WORD)
    lyrics_text.pack(expand=True, fill=tk.BOTH)
    
    lyrics_text.insert(tk.END, song.lyrics)
    lyrics_text.config(state=tk.DISABLED)

# Main window setup
root = tk.Tk()
root.title("Lyrics Finder")

# Song title label and entry
tk.Label(root, text="Song Title:").grid(row=0, column=0, padx=10, pady=10)
song_title_entry = tk.Entry(root, width=30)
song_title_entry.grid(row=0, column=1, padx=10, pady=10)

# Artist name label and entry
tk.Label(root, text="Artist Name (optional):").grid(row=1, column=0, padx=10, pady=10)
artist_name_entry = tk.Entry(root, width=30)
artist_name_entry.grid(row=1, column=1, padx=10, pady=10)

# Search button
search_button = tk.Button(root, text="Search Lyrics", command=get_lyrics)
search_button.grid(row=2, columnspan=2, pady=10)

# Run the application
root.mainloop()