# 🔐 Python Password Manager

A simple, secure desktop password manager built with Python and Tkinter.  
This app helps you store and manage your passwords locally with encryption and a clean interface.

---

## 📦 Features

- ✅ Add, edit, delete, and search passwords  
- ✅ Passwords are encrypted using a simple Caesar cipher (for demonstration purposes)  
- ✅ Password generator with custom options  
- ✅ Master password protection on launch  
- ✅ Auto-saves to a JSON file  
- ✅ GUI built with Tkinter (no browser needed)  
- ✅ Fully packaged as a Windows `.exe` using PyInstaller  

---

## 🖼️ Screenshots

*You can add screenshots or a demo video here in a `screenshots/` folder.*

---

## 🧠 How It Works

1. On first launch, you're asked to set a master password.  
2. The app creates a `passwords.json` file where encrypted passwords are saved.  
3. On future launches, you'll be asked to enter your master password to unlock the manager.  
4. You can add, search, edit, or delete passwords.  
5. You can also generate secure random passwords and copy them to the clipboard.

🔒 All data is stored **locally** and never uploaded online.

---

## 🛠 How to Run

### ▶️ Run from Python

Make sure the following files are in the same folder:
- `main.py`
- `ui.py`
- `logic.py`
- `storage.py`
- `crypto.py`

Then run:

```bash
python main.py
```

---

### 🪄 Run as Executable (EXE)

Use PyInstaller to package the app:

```bash
pip install pyinstaller
pyinstaller --onefile --noconsole main.py
```

The executable will be created in the `dist/` folder as `main.exe`.  
You can double-click it to launch the app.

✅ You do NOT need to include `passwords.json` — the app will generate it automatically.

📌 Note: You don't need to upload the `.exe` to GitHub. If you want to share it, you can host it separately or just share the PyInstaller command above.

---

## 📁 Project Structure

```
password_manager/
├── main.py              → App entry point  
├── ui.py                → UI logic (add/edit/delete/generate)  
├── logic.py             → Search and result listbox logic  
├── storage.py           → Load/save encrypted passwords  
├── crypto.py            → Caesar cipher encrypt/decrypt  
├── passwords.json       → Auto-generated on first run  
├── README.md            → This file  
└── icon.ico             → (Optional) App icon  
```

---

## ⚙️ Requirements

- Python 3.x  
- Tkinter (included with Python)  
- PyInstaller (optional, for creating `.exe`)

> This app uses only Python’s standard libraries: `tkinter`, `json`, `os`, and `sys`.  
> No external libraries are needed to run the app.

To install PyInstaller (if needed):

```bash
pip install pyinstaller
```

---

## ⚠️ Disclaimer

This project uses a simple Caesar cipher, which is **not secure for real-world use**.  
It is intended for **learning, lightweight personal use, or showcasing your programming skills**.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🧑‍💻 Author

**Youssef** – Python Developer & Freelancer  
[Hire me on Fiverr](https://www.fiverr.com/s/99WP3dd)

If you found this project helpful or inspiring, feel free to ⭐️ the repo or fork it!
