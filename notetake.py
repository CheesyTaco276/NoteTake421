import tkinter as tk
from tkinter import messagebox
import os

def save_note():
    # Save the note to a file in the user's home directory
    save_path = os.path.expanduser("~/notetake421_note.txt")
    with open(save_path, "w") as f:
        f.write(text_area.get("1.0", tk.END))
    messagebox.showinfo("Saved", f"Note saved to {save_path}!")

root = tk.Tk()
root.title("NoteTake421 - Testing")
root.geometry("400x300")

text_area = tk.Text(root)
text_area.pack(expand=True, fill='both')

save_btn = tk.Button(root, text="Save Note", command=save_note)
save_btn.pack()

root.mainloop()
