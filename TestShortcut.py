import threading
import keyboard
import pyperclip
import tkinter as tk
from tkinter import messagebox

# Dictionary to store hotkeys and associated text
shortcuts = {}

def copy_text(text):
    """Copy the provided text to the clipboard."""
    pyperclip.copy(text)
    text_display.delete("1.0", tk.END)  # Clear the text area
    text_display.insert(tk.END, text)   # Show copied text
    print(f"[INFO] Copied to clipboard: {text}")

def add_shortcut():
    """Add a new shortcut from the input fields."""
    hotkey = hotkey_entry.get().strip()
    text = text_entry.get().strip()

    if not hotkey or not text:
        messagebox.showerror("Error", "Both hotkey and text fields must be filled!")
        return

    # If hotkey already exists, remove the old one
    if hotkey in shortcuts:
        keyboard.remove_hotkey(shortcuts[hotkey]['id'])

    # Register the hotkey
    hotkey_id = keyboard.add_hotkey(hotkey, lambda: copy_text(text))
    shortcuts[hotkey] = {'text': text, 'id': hotkey_id}

    # Update the listbox
    update_listbox()

def remove_shortcut():
    """Remove the selected shortcut from the listbox and the dictionary."""
    selected = listbox.curselection()
    if not selected:
        return
    
    hotkey = listbox.get(selected[0])
    if hotkey in shortcuts:
        keyboard.remove_hotkey(shortcuts[hotkey]['id'])
        del shortcuts[hotkey]

    update_listbox()

def update_listbox():
    """Refresh the listbox with the current hotkeys."""
    listbox.delete(0, tk.END)
    for hotkey, data in shortcuts.items():
        listbox.insert(tk.END, hotkey)

def on_select(event):
    """Display selected shortcut's text in the entry field."""
    selected = listbox.curselection()
    if not selected:
        return
    hotkey = listbox.get(selected[0])
    text_entry.delete(0, tk.END)
    text_entry.insert(0, shortcuts[hotkey]['text'])

# Create the GUI (Must run in the main thread)
root = tk.Tk()
root.title("Shortcut Manager")

# Hotkey Entry
tk.Label(root, text="Hotkey:").grid(row=0, column=0)
hotkey_entry = tk.Entry(root, width=20)
hotkey_entry.grid(row=0, column=1)

# Text Entry
tk.Label(root, text="Text:").grid(row=1, column=0)
text_entry = tk.Entry(root, width=40)
text_entry.grid(row=1, column=1)

# Buttons
add_button = tk.Button(root, text="Add Shortcut", command=add_shortcut)
add_button.grid(row=2, column=0, columnspan=2, pady=5)

remove_button = tk.Button(root, text="Remove Selected", command=remove_shortcut)
remove_button.grid(row=3, column=0, columnspan=2, pady=5)

# Listbox for shortcuts
tk.Label(root, text="Active Shortcuts:").grid(row=4, column=0)
listbox = tk.Listbox(root, height=10, width=30)
listbox.grid(row=4, column=1)
listbox.bind("<<ListboxSelect>>", on_select)

# Text Display for copied text
tk.Label(root, text="Copied Text:").grid(row=5, column=0)
text_display = tk.Text(root, height=3, width=40)
text_display.grid(row=5, column=1)

# Function to listen for ESC key in a separate thread
def listen_for_esc():
    print("[SYSTEM] Background script running. Use the GUI to manage shortcuts.")
    keyboard.wait('esc')
    print("[SYSTEM] Exiting script.")
    root.quit()

# Start the keyboard listener in a separate thread
esc_listener_thread = threading.Thread(target=listen_for_esc, daemon=True)
esc_listener_thread.start()

# Run Tkinter (in the main thread)
root.mainloop()
