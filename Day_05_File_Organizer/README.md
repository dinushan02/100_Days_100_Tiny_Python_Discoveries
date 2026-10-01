# 📁 Day 05 — File Organizer

Part of the **100 Days, 100 Tiny Python Discoveries** series.

This project demonstrates how Python can automatically organize files into separate folders based on their file extensions.

For example, instead of having many different files mixed together:

```text
downloads/
├── photo.jpg
├── resume.pdf
├── notes.txt
├── song.mp3
└── script.py
```

Python can organize them into:

```text
downloads/
├── JPG/
│   └── photo.jpg
├── PDF/
│   └── resume.pdf
├── TXT/
│   └── notes.txt
├── MP3/
│   └── song.mp3
└── PY/
    └── script.py
```

This is a small example of how Python can be used for real-world file automation.

---

## 🎯 Objective

The goal of this project is to learn how Python can:

- Work with files and folders
- Read the contents of a directory
- Check whether an item is a file
- Get a file's extension
- Create folders automatically
- Move files between folders
- Use loops and conditions for automation
- Build a simple file-management script

---

## 🧠 Python Concepts Used

- `import`
- `os` module
- `shutil` module
- Variables
- `for` loops
- `if` statements
- File paths
- File extensions
- `os.listdir()`
- `os.path.join()`
- `os.path.isfile()`
- `os.path.splitext()`
- `os.makedirs()`
- `shutil.move()`
- `exist_ok=True`

---

## 💻 Complete Code

```python
"""
Organize files into folders based on their file extensions.
"""

import os
import shutil

source_folder = "downloads"

for file in os.listdir(source_folder):
    file_path = os.path.join(source_folder, file)

    if os.path.isfile(file_path):
        extension = os.path.splitext(file)[1].lower()

        if extension:
            folder_name = extension[1:].upper()
            folder_path = os.path.join(source_folder, folder_name)

            os.makedirs(folder_path, exist_ok=True)

            shutil.move(file_path, os.path.join(folder_path, file))

print("Files organized successfully!")
```

---

## 🔍 Line-by-Line Explanation

### 1. Docstring

```python
"""
Organize files into folders based on their file extensions.
"""
```

This is a short description of what the program does. It helps other developers understand the purpose of the file when they open it.

It is written using triple quotes, so Python treats it as a multi-line string. When it appears at the very top of a file, it is called a **docstring**.

### 2. Import the `os` Module

```python
import os
```

`os` is a Python module that allows us to interact with the operating system.

We use it in this project to work with:

- Files
- Folders
- Directory contents
- File paths

For example, we use:

```python
os.listdir()
```

to see the files inside a folder.

### 3. Import the `shutil` Module

```python
import shutil
```

`shutil` provides useful operations for working with files and directories.

In this project, we use:

```python
shutil.move()
```

to move files from one location to another.

### 4. Set the Source Folder

```python
source_folder = "downloads"
```

Here, we store the name of the folder that contains the files we want to organize.

Instead of writing `"downloads"` many times throughout the program, we store it in a variable:

```text
source_folder
        ↓
"downloads"
```

This makes the code easier to read and change. For example, if you wanted to organize a folder called `documents`, you could change it to:

```python
source_folder = "documents"
```

### 5. Get Files from the Folder

```python
for file in os.listdir(source_folder):
```

This line does two things.

**`os.listdir()`**

```python
os.listdir(source_folder)
```

returns the names of all items inside the `downloads` folder. For example:

```python
["photo.jpg", "resume.pdf", "notes.txt", "script.py"]
```

**`for`**

The `for` loop processes each item one at a time. So Python effectively does:

```text
photo.jpg
resume.pdf
notes.txt
script.py
```

one after another. The variable `file` represents the current item being processed.

### 6. Create the Full File Path

```python
file_path = os.path.join(source_folder, file)
```

Here we create the complete path to the current file. For example:

```python
source_folder = "downloads"
file = "photo.jpg"
```

The result becomes:

```text
downloads/photo.jpg
```

We use `os.path.join()` instead of manually writing `/` or `\`, because different operating systems use different path separators. `os.path.join()` handles this appropriately.

### 7. Check Whether It Is a File

```python
if os.path.isfile(file_path):
```

A folder can contain both files and directories. For example:

```text
downloads/
├── photo.jpg
├── resume.pdf
└── old_files/
```

We only want to organize actual files. So:

```python
os.path.isfile(file_path)
```

checks whether the current path points to a file. If it is a file, the code inside the `if` block runs.

### 8. Get the File Extension

```python
extension = os.path.splitext(file)[1].lower()
```

This line gets the file extension. For example, `photo.jpg` has `.jpg` as its extension.

**`os.path.splitext()`**

This separates the filename into two parts: the name and the extension.

```python
os.path.splitext("photo.jpg")
```

returns:

```python
("photo", ".jpg")
```

The `[1]` selects the second part:

```python
".jpg"
```

**Why use `.lower()`?**

`.lower()` converts the extension to lowercase. For example, `.JPG` becomes `.jpg` and `.PDF` becomes `.pdf`. This keeps file types consistent, so `photo.JPG` and `photo.jpg` end up in the same folder.

### 9. Check Whether an Extension Exists

```python
if extension:
```

Some files may not have an extension. For example, a file named `README` doesn't have `.txt`, `.pdf`, `.jpg`, etc.

This condition makes sure we only continue when an extension exists. Files without an extension are skipped and stay where they are.

### 10. Create the Folder Name

```python
folder_name = extension[1:].upper()
```

Suppose the extension is `.jpg`. We want the folder to be `JPG`.

**`[1:]`** removes the first character, which is the dot:

```text
.jpg
 ↓
jpg
```

**`.upper()`** then converts it to uppercase:

```text
jpg
 ↓
JPG
```

So `.jpg` becomes `JPG`.

### 11. Create the Folder Path

```python
folder_path = os.path.join(source_folder, folder_name)
```

Now we create the complete path for the new folder. For example:

```python
source_folder = "downloads"
folder_name = "JPG"
```

The result becomes:

```text
downloads/JPG
```

### 12. Create the Folder

```python
os.makedirs(folder_path, exist_ok=True)
```

This creates the folder if it doesn't already exist. For example:

```text
downloads/JPG
```

If the `JPG` folder already exists, we don't want Python to produce an error. That's why we use:

```python
exist_ok=True
```

It means:

> Create the folder if it doesn't exist. If it already exists, continue without raising an error.

Without `exist_ok=True`, trying to create an existing folder would cause an error.

### 13. Move the File

```python
shutil.move(file_path, os.path.join(folder_path, file))
```

This is the line that actually moves the file. Let's break it down.

**Source**

```python
file_path
```

This is where the file currently exists, for example `downloads/photo.jpg`.

**Destination**

```python
os.path.join(folder_path, file)
```

This creates the new location, for example `downloads/JPG/photo.jpg`.

**`shutil.move()`**

Python then moves `downloads/photo.jpg` to `downloads/JPG/photo.jpg`.

### 14. Success Message

```python
print("Files organized successfully!")
```

After all files have been processed, Python displays:

```text
Files organized successfully!
```

This lets the user know that the program has finished.

---

## 🔄 How the Program Works

The complete process looks like this:

```text
Start
  ↓
Open the downloads folder
  ↓
Get all items
  ↓
Check each item
  ↓
Is it a file?
  ↓
Yes
  ↓
Get the file extension
  ↓
Create a folder for the extension
  ↓
Move the file
  ↓
Process the next file
  ↓
All files completed
  ↓
Display success message
  ↓
End
```

---

## 📂 Example

### Before Running the Program

Suppose the `downloads` folder contains:

```text
downloads/
├── photo.jpg
├── resume.pdf
├── notes.txt
├── song.mp3
└── script.py
```

The files are all mixed together.

### After Running the Program

Python organizes them:

```text
downloads/
│
├── JPG/
│   └── photo.jpg
│
├── PDF/
│   └── resume.pdf
│
├── TXT/
│   └── notes.txt
│
├── MP3/
│   └── song.mp3
│
└── PY/
    └── script.py
```

Terminal:

```text
Files organized successfully!
```

---

## ▶️ How to Run

### Step 1 — Create the Folder

Create a folder named `downloads` and place some test files inside it. For example:

```text
downloads/
├── photo.jpg
├── resume.pdf
├── notes.txt
└── script.py
```

### Step 2 — Run the Python Program

From the project directory (the folder that **contains** `downloads/`), run:

```bash
python file_organizer.py
```

### Step 3 — Check the Result

Open the `downloads` folder and check the newly created folders.

---

## ⚠️ Important Safety Note

This program **moves** files. That means the original files will no longer remain directly inside the `downloads` folder.

- For learning, always test the program using a test folder with sample files first.
- Do not point the program at an important folder until you fully understand what it does.
- Keep `file_organizer.py` **outside** the folder being organized. Otherwise it would move itself into `PY/`.
- If a file with the same name already exists in the destination folder, the result depends on your operating system: it may be overwritten or an error may be raised.

---

## 🧠 What I Learned

Through this small project, I learned how to:

- Import Python modules
- Work with the operating system
- Read directory contents
- Work with file paths
- Check whether an item is a file
- Extract file extensions
- Create directories
- Move files
- Use `for` loops
- Use `if` conditions
- Automate repetitive file-management tasks

---

## 🚀 Why This Is Useful for Python Development

This project is more than just a small script. It introduces the idea of **automation**.

Instead of manually moving hundreds of files into different folders, Python can perform the repetitive work automatically.

The same concepts can later be used in larger applications such as:

- File management tools
- Backup systems
- Data-processing scripts
- Automation tools
- Document management systems
- Batch-processing applications

---

## 🔧 Possible Improvements

This project can be improved in many ways. Future versions could support:

- User-selected folders
- Custom folder names
- Multiple file extensions
- Duplicate file handling
- Hidden files
- Error handling
- Logging
- Command-line arguments
- Recursive folder organization
- A graphical user interface

---

## 📚 Key Functions Used

| Function | Purpose |
|---|---|
| `os.listdir()` | Gets items inside a directory |
| `os.path.join()` | Creates file and folder paths |
| `os.path.isfile()` | Checks whether a path is a file |
| `os.path.splitext()` | Separates filename and extension |
| `os.makedirs()` | Creates directories |
| `shutil.move()` | Moves files |
| `.lower()` | Converts text to lowercase |
| `.upper()` | Converts text to uppercase |

---

## 🐍 About This Discovery

This project is **Day 05** of:

**100 Days, 100 Tiny Python Discoveries**

The goal of this journey is to learn Python through small, practical discoveries.

> Learn → Code → Run → Understand → Discover

---

## 📌 Project Information

- **Day:** 05
- **Topic:** File Organizer
- **Language:** Python
- **Modules:** `os`, `shutil`
- **Difficulty:** Beginner
- **Category:** File System Automation

---

## 🗂️ Final Structure

```text
Day_05_File_Organizer/
│
├── file_organizer.py
└── README.md
```