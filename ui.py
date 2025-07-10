from tkinter import *
from tkinter import messagebox, ttk
import storage
import logic
import crypto
import random


def focusin(event, search):
    """
    Clears placeholder text in the search bar when focused.
    """
    if search.get() == "Search for an app...":
        search.delete(0, END)


def focusout(event, search):
    """
    Restores placeholder text if the search bar is empty on focus out.
    """
    if search.get().strip() == "":
        search.insert(0, "Search for an app...")


def add(result, saved_objs):
    """
    Opens a window to add a new app and password to the manager.
    """

    def enter(win):
        if app_entry.get().strip() == "" or password_entry.get().strip() == "":
            messagebox.showwarning("Empty Field", "Please fill in both fields.")
            return

        if app_entry.get() in saved_objs["passwords"]:
            messagebox.showwarning("Duplicate App", "This app already exists. Use Edit instead.")
            return

        # Save new encrypted password
        saved_objs["passwords"][app_entry.get()] = crypto.encrypt(password_entry.get())
        storage.save_to_file(saved_objs)
        logic.show_apps(result, saved_objs)
        win.destroy()

    def show():
        # Toggle password visibility
        if password_entry.cget("show") == "*":
            password_entry.config(show="")
        else:
            password_entry.config(show="*")

    adding_window = Toplevel()
    adding_window.title("Add Password")
    adding_window.geometry("200x200")
    adding_window.bind("<Return>", lambda e: enter(adding_window))

    ttk.Label(adding_window, text="Enter the app").pack()
    app_entry = ttk.Entry(adding_window)
    app_entry.pack(pady=5)

    ttk.Label(adding_window, text="Enter the password").pack(pady=5)
    password_entry = ttk.Entry(adding_window, show="*")
    password_entry.pack(pady=5)

    ttk.Button(adding_window, text="Show", command=show).pack()
    ttk.Button(adding_window, text="Done", command=lambda: enter(adding_window)).pack()


def delete(result, saved_objs):
    """
    Deletes the selected app from the password manager.
    """
    selected = result.curselection()
    if not selected:
        return

    try:
        app = result.get(selected[0])
        confirm = messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete {app}?")
        if confirm:
            del saved_objs["passwords"][app]
            storage.save_to_file(saved_objs)
            logic.show_apps(result, saved_objs)
    except Exception as e:
        messagebox.showerror("Delete Error", f"Could not delete:\n{e}")


def edit(result, saved_objs):
    """
    Opens a window to edit the password of a selected app.
    """

    def save():
        saved_objs["passwords"][app] = crypto.encrypt(password_entry.get())
        storage.save_to_file(saved_objs)
        logic.show_apps(result, saved_objs)
        edit_window.destroy()

    def show():
        if password_entry.cget("show") == "*":
            password_entry.config(show="")
        else:
            password_entry.config(show="*")

    selected = result.curselection()
    if not selected:
        return

    app = result.get(selected[0])
    edit_window = Toplevel()
    edit_window.title("Edit Password")
    edit_window.bind("<Return>", lambda e: save())

    ttk.Label(edit_window, text=f"App: {app}").pack()
    ttk.Label(edit_window, text="Enter new password:").pack()
    password_entry = ttk.Entry(edit_window, show="*")
    password_entry.pack()

    ttk.Button(edit_window, text="Show", command=show).pack()
    ttk.Button(edit_window, text="Save", command=save).pack()


def show_password(event, result, saved_objs):
    """
    Shows the decrypted password for the selected app in a popup window.
    """
    selected = result.curselection()
    if not selected:
        return

    app = result.get(selected[0])
    password = crypto.decrypt(saved_objs["passwords"][app])

    password_window = Toplevel()
    password_window.title(app)

    ttk.Label(password_window, text=f"App: {app}").pack()
    ttk.Label(password_window, text=f"Password: {password}").pack()
    ttk.Button(password_window, text="Ok", command=password_window.destroy).pack()


def generate_password(result, saved_objs):
    """
    Opens a password generator tool that lets the user create and copy strong passwords.
    """
    generating_window = Toplevel()
    generating_window.title("Password Generator")
    generating_window.geometry("300x400")

    generated_password = ""

    def generate():
        nonlocal generated_password
        try:
            length = int(entry.get())
            if length < 1:
                return
        except ValueError:
            return

        characters = ""
        if letter_var.get():
            characters += letters
        if number_var.get():
            characters += numbers
        if symbol_var.get():
            characters += symbols

        if characters.strip():
            generated_password = ''.join(random.choices(characters, k=length))
            password_label.config(text=generated_password)
        else:
            password_label.config(text="Please select at least one option.")

        logic.show_apps(result, saved_objs)

    def copy():
        if generated_password:
            generating_window.clipboard_clear()
            generating_window.clipboard_append(generated_password)
            messagebox.showinfo("Password Generator", "Password copied to clipboard")
            generating_window.destroy()

    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "1234567890"
    symbols = "!@#$%^&*()_-[]{}'\"\\/.,<>?:;|`~"

    Label(generating_window, text="Password Generator", font=("Arial", 16)).pack(pady=10)

    Label(generating_window, text="Enter password length:").pack()
    entry = Entry(generating_window)
    entry.pack(pady=5)

    letter_var = IntVar()
    number_var = IntVar()
    symbol_var = IntVar()

    Label(generating_window, text="Include:").pack(pady=10)
    Checkbutton(generating_window, text="Letters", variable=letter_var).pack()
    Checkbutton(generating_window, text="Numbers", variable=number_var).pack()
    Checkbutton(generating_window, text="Symbols", variable=symbol_var).pack()

    Button(generating_window, text="Generate", command=generate).pack(pady=10)

    password_label = Label(generating_window, font=("Arial", 12), wraplength=280)
    password_label.pack(pady=10)

    Button(generating_window, text="Copy to clipboard", command=copy).pack()
