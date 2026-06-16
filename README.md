# 📝 Auto-Folder File Editor

A lightweight, user-friendly desktop application built with Python's Tkinter that allows you to browse, view, and edit text files within a directory and its subdirectories — all from a simple graphical interface.

![Python Version](https://img.shields.io/badge/python-3.6+-blue.svg)
![Tkinter](https://img.shields.io/badge/Tkinter-GUI-green.svg)
![License](https://img.shields.io/badge/license-MIT-yellow.svg)

---

## ✨ Features

- 🚀 **Automatic Folder Detection** – Detects the folder where the script is running
- 📂 **Subfolder Support** – Lists all text files from the current directory and subdirectories
- 🔍 **Easy File Selection** – Dropdown menu for quick file switching
- 📝 **In-App Editing** – View and edit file content directly
- 💾 **One-Click Save** – Save changes instantly with visual feedback
- 🎨 **Clean UI** – Simple and intuitive interface

---

## 🖥️ User Interface

<img width="867" height="717" alt="image" src="https://github.com/user-attachments/assets/3da8d719-ad97-45db-a0d0-2d1df04a1764" />


```
+---------------------------------------------------+
|  📂 Auto-Folder File Editor                       |
+---------------------------------------------------+
|  Working Directory: /path/to/your/folder          |
|                                                    |
|  Select File from Folder or Subfolders:            |
|  [Dropdown ▼]                                     |
|                                                    |
|  File Content (Paste here):                        |
|  +---------------------------------------------+  |
|  |                                             |  |
|  |  Your file content appears here...          |  |
|  |                                             |  |
|  +---------------------------------------------+  |
|                                                    |
|  [ 💾 Save Content ]                              |
+---------------------------------------------------+
```

---

## 🚀 Installation

### Prerequisites
- Python 3.6 or higher
- Tkinter (comes pre-installed with Python on most systems)

### Quick Start

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/auto-folder-file-editor.git
cd auto-folder-file-editor
```

2. **Run the application**
```bash
python file_edit.py
```

3. **(Optional) Create a .bat file for Windows**
Create a `launch.bat` file in the same directory:
```batch
@echo off
python file_edit.py
pause
```

---

## 📖 How It Works

### Core Logic

1. **Directory Scanning** – The app automatically scans the directory where `file_edit.py` is located and all its subdirectories.

2. **File Discovery** – It collects all files (except the script itself and `.bat` files) and displays them in a dropdown.

3. **File Reading** – When you select a file, it reads the content and displays it in the text area using UTF-8 encoding.

4. **Editing & Saving** – You can modify the content in the text area and save it back to the file.

### Key Code Snippets

```python
# Automatic folder detection
self.current_folder = os.path.dirname(os.path.abspath(__file__))

# Scanning subdirectories
for root_dir, dirs, files in os.walk(self.current_folder):
    for file in files:
        if file == "editor.py" or file.endswith(".bat"):
            continue
        full_path = os.path.join(root_dir, file)
        rel_path = os.path.relpath(full_path, self.current_folder)
        self.file_map[rel_path] = full_path
        file_list.append(rel_path)
```

---

## 🎯 Use Cases

- 📄 **Configuration File Management** – Edit `.ini`, `.cfg`, `.json` files in your project
- 📝 **Note Taking** – Quick text file editing without opening a full IDE
- 📂 **Project File Management** – Browse and update documentation files
- 🧪 **Testing** – Modify test data files on the fly

---

## ⚙️ Configuration

### Supported File Types
The app supports **all text-based files** that can be read with UTF-8 encoding. This includes:

- `.txt`, `.log`, `.md`
- `.py`, `.js`, `.html`, `.css`
- `.json`, `.xml`, `.yaml`
- `.ini`, `.cfg`, `.conf`
- And more...

### File Exclusions
The app automatically excludes:
- The script itself (`editor.py`)
- Any `.bat` files (to prevent accidental modifications)

---

## 🛠️ Troubleshooting

### Common Issues

| Issue | Solution |
|-------|----------|
| **No files found** | Make sure there are text files in the directory or subdirectories |
| **Encoding errors** | The app tries UTF-8 with `errors='ignore'` to handle various encodings |
| **Can't save file** | Check file permissions – you need write access to the file |
| **Blank text area** | The file might be empty or contain non-UTF-8 characters |

### Error Handling
- ✅ File read errors show a descriptive message
- ✅ Save errors display the specific exception
- ✅ Empty folders trigger a warning notification

---

## 📁 Project Structure

```
auto-folder-file-editor/
├── file_edit.py          # Main application
├── README.md             # This file
├── LICENSE               # MIT License
└── examples/             # Sample files
    ├── config.txt
    └── notes.md
```

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/AmazingFeature`)
3. **Commit** your changes (`git commit -m 'Add some AmazingFeature'`)
4. **Push** to the branch (`git push origin feature/AmazingFeature`)
5. **Open** a Pull Request

### Ideas for Improvement

- [ ] Add dark mode support
- [ ] Implement file search/filter functionality
- [ ] Add syntax highlighting for code files
- [ ] Support for drag-and-drop files
- [ ] Auto-save feature
- [ ] File encoding selection
- [ ] Recent files history

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

---

## 👤 Author

**DEBANJAN PAL**
---

## 🙏 Acknowledgments

- Built with Python's built-in Tkinter library
- Inspired by the need for simple, folder-based text editing
- Thanks to all open-source contributors

---

## 📌 Version History

### v1.0.0 (Current)
- Initial release
- Basic file browsing and editing
- Subfolder support
- UTF-8 encoding handling

---

## 🔮 Future Plans

- 🔒 **File Locking** – Prevent concurrent edits
- 🌐 **Multi-language Support** – Internationalization
- 📊 **File Stats** – Show file size, line count, etc.
- 🔄 **Auto-refresh** – Detect external file changes
- ⌨️ **Keyboard Shortcuts** – For power users

---

## 💡 Tips

1. **Quick Access** – Place the script in your project folder and create a shortcut
2. **Batch Editing** – Use it to quickly update multiple text files in a project
3. **Backup** – Consider backing up files before making bulk edits

---

*Made with ❤️ for developers who love simplicity*
