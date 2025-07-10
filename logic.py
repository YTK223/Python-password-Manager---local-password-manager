from tkinter import END

def search_function(result, search, saved_objs):
    """
    Searches for applications stored in the password manager and displays matching results.

    Args:
        result (tk.Listbox): The widget where search results are displayed.
        search (tk.Entry): The entry widget containing the search query.
        saved_objs (dict): The dictionary containing saved passwords in this format:
                           {"passwords": {"app_name": {"username": ..., "password": ...}}}
    """
    result.delete(0, END)  # Clear current listbox contents
    search_text = search.get().lower()  # Get the user's input and make it lowercase

    if search_text.strip() == "":
        # If the search is empty, show all saved apps
        show_apps(result, saved_objs)
        return

    # Loop through saved apps and add those that match the search
    for app in saved_objs["passwords"].keys():
        if search_text in app.lower():
            result.insert(END, app)


def show_apps(result, saved_objs):
    """
    Displays all saved application names in the result listbox.

    Args:
        result (tk.Listbox): The widget to display the app names.
        saved_objs (dict): The dictionary containing saved passwords.
    """
    result.delete(0, END)  # Clear the listbox first

    if saved_objs.get("passwords", False):
        # Insert each app name into the listbox
        for app in saved_objs["passwords"].keys():
            result.insert(END, app)
