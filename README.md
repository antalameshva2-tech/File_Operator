# 📔 Personal Journal Manager (File Operator)

## 👨‍💻 Author

### **Antala Meshva**

🐍 **Python Learner** | 💻 **Developer** | 📚 **Student**

---

## 📌 About the Project

**Personal Journal Manager (File Operator)** is a beginner-friendly Python application designed to manage personal journal entries using **File Handling** and **Object-Oriented Programming (OOP)** concepts.

The application allows users to:

- ✍️ Add new journal entries
- 📖 View today's journal entries
- 🔍 Search journal entries
- 🗑️ Delete all journal entries
- ⏰ Automatically store date and time

All journal entries are stored in a text file named:

```text
journal.txt
```

The main purpose of this project is to understand how Python **File Operators / File Modes** work in a practical application.

---

# ✨ Features

- ✍️ **Add a New Entry**
- 📖 **View Today's Entries**
- 🔍 **Search an Entry**
- 🗑️ **Delete All Entries**
- ⏰ **Automatic Timestamp**
- 📄 **Text File Storage**
- 🛡️ **Error Handling**
- 🧱 **Object-Oriented Programming**
- 🎯 **Simple Menu-Based Interface**

---

# 🛠️ Technologies Used

- 🐍 Python
- 📂 File Handling
- 🧱 Object-Oriented Programming
- ⏰ `datetime`
- ⌛ `time`
- 🛡️ Exception Handling
- 💻 Command Line Interface

---

# 📂 File Handling

File Handling is the main concept of this project.

The program uses four different file modes:

| File Mode | Operation | Purpose |
|:---:|---|---|
| `x` | Create | Creates a new file |
| `a` | Append | Adds new entries at the end |
| `r` | Read | Reads and searches entries |
| `w` | Write | Clears all existing entries |

### 🔄 File Mode Flow

```text
"x" → Create File
        ↓
"a" → Add Journal Entries
        ↓
"r" → Read / Search Entries
        ↓
"w" → Delete All Entries
```

---

# 🧱 Object-Oriented Programming

The project uses a class named:

```python
class JournalManager:
```

The class contains different methods for managing journal entries.

### Main Methods

```text
JournalManager
│
├── __init__()
├── add_entry()
├── view_entries()
├── search_entry()
├── delete_entries()
├── show_menu()
└── run()
```

---

# 📁 Project Structure

```text
Personal-Journal-Manager/
│
├── journal_manager.py
├── journal.txt
└── README.md
```

### 📄 `journal_manager.py`

Contains the complete Python source code.

### 📄 `journal.txt`

Stores all journal entries.

> `journal.txt` is created automatically when required.

### 📄 `README.md`

Contains complete project documentation.

---

# ⚙️ How the Project Works

## 1️⃣ Add a New Entry

Select:

```text
1. Add a New Entry
```

The program asks:

```text
Enter your journal entry:
```

Example:

```text
Today I learned Python File Handling.
```

The program automatically adds the current date and time.

Example:

```text
[2026-10-02 14:10:25]
Today I learned Python File Handling.
```

The entry is stored using **`a` (append) mode**, so old entries remain safe.

---

## 2️⃣ View All Entries

Select:

```text
2. View All Entries
```

The program opens the file using **`r` (read) mode**.

Only entries created on **today's date** are displayed.

The latest entry is displayed first.

### Example

```text
Your Journal Entries:
---------------------------------

[2026-10-02 14:10:25]
Today I learned Python File Handling.

[2026-10-02 13:45:12]
Started working on my journal project.
```

---

## 3️⃣ Search for an Entry

Select:

```text
3. Search for an Entry
```

The program asks:

```text
Enter a keyword or date to search:
```

The user can search using:

- 🔤 Keyword
- 📅 Date
- 📝 Part of the journal text

### Example

```text
Enter a keyword or date to search:
Python
```

The program displays matching entries.

### 🔤 Case-Insensitive Search

The search works with different letter cases:

```text
python
Python
PYTHON
```

All can match the same keyword.

---

## 4️⃣ Delete All Entries

Select:

```text
4. Delete All Entries
```

The program asks for confirmation:

```text
Are you sure you want to delete all entries? (yes/no):
```

If the user enters:

```text
yes
```

the program uses:

```python
open(self.filename, "w")
```

The **`w` mode** clears all existing journal entries.

### ⚠️ Important

The `journal.txt` file remains, but all existing content inside it is erased.

---

## 5️⃣ Exit

Select:

```text
5. Exit
```

The program displays:

```text
Thank you for using Personal Journal Manager. Goodbye!
```

Then the application stops.

---

# 🖥️ Main Menu

When the program starts:

```text
Welcome to Personal Journal Manager!
Please select an option:

1. Add a New Entry
2. View All Entries
3. Search for an Entry
4. Delete All Entries
5. Exit
```

---

# 📄 Journal File Format

All journal entries are stored inside:

```text
journal.txt
```

Example:

```text
[2026-10-02 14:10:25]
Today I learned Python File Handling.

[2026-10-02 13:45:12]
I worked on my journal project.

[2026-10-01 18:20:45]
Started learning File Handling.
```

Each entry contains:

```text
[Date & Time]
Journal Text
```

---

# ⏰ Timestamp System

Every journal entry automatically receives a timestamp.

The project uses:

```python
timestamp = time.time()
```

Then:

```python
datetime.fromtimestamp(timestamp)
```

The timestamp is displayed in:

```text
YYYY-MM-DD HH:MM:SS
```

Example:

```text
[2026-10-02 14:10:25]
```

---

# 🛡️ Error Handling

The project uses `try-except` to handle common errors.

## ❌ Empty Entry

If the user enters an empty journal entry:

```text
Error: Entry cannot be empty.
Please write something and try again.
```

---

## ❌ File Not Found

If `journal.txt` does not exist:

```text
Error: The journal file does not exist.
Please add a new entry first.
```

---

## 🔐 Permission Error

If the file cannot be accessed:

```text
Error: Permission denied.
Please check the file permissions.
```

---

## ❌ Empty Search Keyword

If the user enters an empty keyword:

```text
Error: Keyword cannot be empty.
Please enter a word or a date (YYYY-MM-DD).
```

---

## ❌ Invalid Menu Option

If the user enters an invalid option:

```text
Invalid option.
Please select a valid option from the menu.
```

---

## ❌ Invalid Delete Confirmation

The program accepts:

```text
yes
no
```

If another value is entered:

```text
Invalid input.
Please type yes or no.
```

---

# 📦 Modules Used

The project uses only Python's built-in modules:

```python
import os
import time
from datetime import datetime
```

### No External Libraries Required

The project can run without installing any additional packages.

---

# 💻 Requirements

Before running the project, make sure Python is installed.

### Requirements

- Python 3.x
- Python IDE or Code Editor
- Terminal / Command Prompt
- Windows, Linux, or macOS

### Check Python Version

```bash
python --version
```

or:

```bash
python3 --version
```

---

# ▶️ How to Run

### Step 1 — Open the Project

Open the folder containing:

```text
journal_manager.py
```

### Step 2 — Open Terminal

Navigate to the project folder.

### Step 3 — Run the Program

```bash
python journal_manager.py
```

For systems using `python3`:

```bash
python3 journal_manager.py
```

### Step 4 — Select an Option

```text
1 → Add Entry
2 → View Entries
3 → Search Entry
4 → Delete All Entries
5 → Exit
```

---

# 🔄 Program Flow

```text
             ┌──────────────────────┐
             │     Start Program    │
             └──────────┬───────────┘
                        ↓
             ┌──────────────────────┐
             │      Show Menu       │
             └──────────┬───────────┘
                        ↓
             ┌──────────────────────┐
             │    User Selection    │
             └──────────┬───────────┘
                        ↓
       ┌────────┬────────┬────────┬────────┐
       ↓        ↓        ↓        ↓        ↓
     Add      View     Search   Delete    Exit
       ↓        ↓        ↓        ↓        ↓
     Save     Read     Find     Clear     Close
       ↓        ↓        ↓        ↓
       └────────┴────────┴────────┘
                        ↓
                   Show Menu
```

---

# 🧩 Method Description

| Method | Purpose |
|---|---|
| `__init__()` | Initializes the journal file |
| `add_entry()` | Adds a new journal entry |
| `view_entries()` | Displays today's entries |
| `search_entry()` | Searches journal entries |
| `delete_entries()` | Clears all journal entries |
| `show_menu()` | Displays the main menu |
| `run()` | Runs the complete program |

---

# 📚 Python Concepts Learned

This project demonstrates:

- 🐍 Python Basics
- 🧱 Classes
- 👤 Objects
- 🏗️ Constructor
- 🔧 Methods
- 📂 File Handling
- 📄 File Modes
- ⏰ Date & Time
- 🔁 `while` Loop
- 🔀 `if-elif-else`
- ⌨️ User Input
- 🛡️ Exception Handling
- 🔍 String Searching
- 📄 Text File Storage

---

# 🎯 Learning Objective

The main objective of this project is to understand how **File Operators / File Handling** work in Python.

The complete file operation flow is:

```text
Create
  ↓
Add
  ↓
Read
  ↓
Search
  ↓
Delete
```

This project also demonstrates how **OOP and File Handling** can be combined to create a practical Python application.

---

# 🚀 Future Improvements

The project can be extended with:

- 🔐 Password Protection
- ✏️ Edit Individual Entries
- 🗑️ Delete Individual Entries
- 📅 Search by Specific Date
- 📊 Total Entry Counter
- 👥 Multiple User Support
- 🔒 Journal Encryption
- 💾 Automatic Backup
- 🖥️ Graphical User Interface
- 🌐 Web-Based Version

---

# ⚠️ Important Notes

- All journal data is stored in `journal.txt`.
- The file is created automatically when required.
- The **View Entries** option displays today's entries.
- The **Search** option searches the stored journal data.
- The **Delete All** option clears all existing entries.
- Deleted entries cannot be recovered using this program.

---

# 📊 Project Information

| Details | Information |
|---|---|
| 📌 Project Name | Personal Journal Manager (File Operator) |
| 👨‍💻 Author | Antala Meshva |
| 🐍 Language | Python |
| 🎓 Level | Beginner / Student |
| 📂 Main Concept | File Handling |
| 🧱 OOP | Yes |
| 📄 Storage | `journal.txt` |
| 💻 Interface | Command Line Interface |
| 📦 External Libraries | None |

---

# ⭐ Conclusion

**Personal Journal Manager (File Operator)** is a simple and practical Python project created to demonstrate **File Handling, File Modes, OOP, Date & Time, Searching, and Exception Handling**.

It provides a beginner-friendly way to create, store, view, search, and delete personal journal entries using a simple text file.

---

## 🌟 Thank You

Thank you for checking out **Personal Journal Manager (File Operator)**! 📔🐍

> **Learn → Practice → Build → Improve**

---

## 📜 License

This project is created for **educational and learning purposes**.
