from tkinter import *
from tkinter import ttk
from os import path

from storage import load_from_file, get_app_data_path
from logic import show_apps, search_function
import ui

# Path to the JSON file storing passwords
json_path = get_app_data_path("passwords.json")

# Load saved data from the file
saved_objs = load_from_file(json_path)

# Create the main window
window = Tk()
window.title("Password Manager")
window.geometry("400x345")

# Scrollbar for the result Listbox
scrollbar = Scrollbar(window)
scrollbar.pack(side=RIGHT, fill=Y)

# Title label
ttk.Label(window, text="Password Manager", font="arial").pack()

# Search entry box
search = ttk.Entry(window)
search.insert(0, "Search for an app...")
search.bind("<FocusIn>", lambda e: ui.focusin(e, search))     # Clear placeholder on focus
search.bind("<FocusOut>", lambda e: ui.focusout(e, search))   # Restore placeholder if empty
search.pack(pady=5)

# Search button
ttk.Button(
    window,
    text="Search",
    command=lambda: search_function(search, result, saved_objs)
).pack(pady=5)

# Listbox to display results (apps)
result = Listbox(window, yscrollcommand=scrollbar.set)
result.bind("<Double-1>", lambda e: ui.show_password(e, result, saved_objs))  # Show password on double-click
result.pack(pady=10)

# Connect scrollbar to Listbox
scrollbar.config(command=result.yview)

# Display all saved apps at startup
show_apps(result, saved_objs)

# Buttons for actions
ttk.Button(window, text="Add", command=lambda: ui.add(result, saved_objs)).pack(side="left")
ttk.Button(window, text="Edit", command=lambda: ui.edit(result, saved_objs)).pack(side="right")
ttk.Button(window, text="Delete", command=lambda: ui.delete(result, saved_objs)).pack()
ttk.Button(window, text="Generate password", command=lambda: ui.generate_password(result, saved_objs)).pack()

# Start the application loop
if __name__ == "__main__":
    window.mainloop()
