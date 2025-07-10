import json
import sys
from sys import exit
from os import path, getcwd
from tkinter import simpledialog, messagebox

import crypto


def save_to_file(saved_objs):
    """
    Saves the given dictionary to 'passwords.json'.

    Args:
        saved_objs (dict): The data to save (includes main password + app passwords).
    """
    try:
        with open("passwords.json", "w") as file:
            json.dump(saved_objs, file, indent=4)
    except (IOError, OSError) as e:
        messagebox.showerror("Save Error", f"Could not save file:\n{e}")


def load_from_file(json_path):
    """
    Loads password data from the specified JSON path.

    - If file exists, prompts for master password and verifies it.
    - If file doesn't exist, prompts to create a new master password.

    Args:
        json_path (str): Path to the JSON file.

    Returns:
        dict: The saved password data including the encrypted master password.
    """
    if path.exists(json_path):
        try:
            with open(json_path, "r") as file:
                saved_objs = json.load(file)
        except (IOError, json.JSONDecodeError) as e:
            messagebox.showerror("Error", f"Could not read file:\n{e}")
            exit()

        # Prompt user to enter the master password and validate it
        while True:
            main_password = simpledialog.askstring("Password", "Enter the password")
            if main_password is None:
                exit()
            if main_password != crypto.decrypt(saved_objs["main password"]):
                messagebox.showerror("Wrong Password", "The password you entered is wrong")
            else:
                break
    else:
        # No file found, create a new one with a master password
        main_password = simpledialog.askstring("Password", "Enter a password for this app")
        if main_password is None:
            exit()
        saved_objs = {
            "main password": crypto.encrypt(main_password),
            "passwords": {}
        }

    return saved_objs


def get_app_data_path(filename):
    """
    Returns the full file path depending on whether the app is running from PyInstaller or not.

    Args:
        filename (str): The name of the file to generate the path for.

    Returns:
        str: Full path to the file in the correct execution context.
    """
    if hasattr(sys, '_MEIPASS'):
        # If bundled with PyInstaller
        return path.join(getcwd(), filename)
    return filename
