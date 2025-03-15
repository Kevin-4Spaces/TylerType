import tkinter as tk
from pynput import keyboard
import threading
import pystray
from PIL import Image, ImageDraw
import sys

import os
os.environ['TK_SILENCE_DEPRECATION'] = '1'

# Global counter
key_count = 0

def on_key_press(key):
    """Increases the key press counter safely in the main thread"""
    global key_count
    key_count += 1
    window.after(0, update_label)  # Schedule UI update in the main thread

def update_label():
    """Updates the label in the main thread"""
    label.config(text=f"Key Presses: {key_count}")

def start_listener():
    listener = keyboard.Listener(on_press=on_key_press)
    listener.start()
    return listener


# Create the main window
window = tk.Tk()
window.title("Key Counter")
window.geometry("300x150")

label = tk.Label(window, text="Key Presses: 0", font=("Arial", 20))
label.pack(pady=20)

# Add a minimize button
#minimize_button = tk.Button(window, text="Minimize to Tray", command=minimize_to_tray)
#minimize_button.pack()

# Start the key listener in a separate thread
listener_thread = threading.Thread(target=start_listener, daemon=True)
listener_thread.start()

window.mainloop()