# 🔐 Day 03 — Password Generator

Part of the **100 Days, 100 Tiny Python Discoveries** series.

This project demonstrates how Python can be used to generate a random 8-character password using the built-in `random` and `string` modules.

The program combines uppercase letters, lowercase letters, and digits to create a randomly generated password.

---

## 🎯 Objective

The goal of this discovery is to learn how to:

- Import Python's built-in modules
- Work with predefined character sets
- Select random characters
- Combine multiple characters into a string
- Use a loop expression with `join()`
- Display formatted output using an f-string

---

## 🧠 Python Concepts Used

### 1. `import random`

The `random` module provides functions for generating random values.

In this project, we use:

```python
random.choice()
```

to randomly select a character.

### 2. `import string`

The `string` module provides useful predefined string constants.

We use:

```python
string.ascii_letters
```

This contains:

```
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
```

We also use:

```python
string.digits
```

which contains:

```
0123456789
```

### 3. Creating the Character Set

```python
characters = string.ascii_letters + string.digits
```

Here, we combine letters and digits into a single string.

The resulting character set contains:

```
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
0123456789
```

This gives the program a collection of characters to choose from.

### 4. Generating the Password

```python
password = ''.join(random.choice(characters) for _ in range(8))
```

This is the main part of the program.

- `random.choice(characters)` — Randomly selects one character from the `characters` string.
- `for _ in range(8)` — Repeats the selection 8 times. The underscore `_` is used because we don't need the loop variable itself.
- `''.join(...)` — Combines the selected characters into one string.

For example:

```
a
K
7
m
P
2
x
Q
```

becomes:

```
aK7mP2xQ
```

### 5. Displaying the Password

```python
print(f"Your generated password is: {password}")
```

The `f` before the string creates an f-string. It allows the value stored in `password` to be inserted directly into the output.

---

## 💻 Complete Code

```python
"""
Generate a random 8-character password
using Python's built-in random and string modules.
"""

import random
import string

characters = string.ascii_letters + string.digits

password = ''.join(random.choice(characters) for _ in range(8))

print(f"Your generated password is: {password}")
```

---

## ▶️ Example Output

```
Your generated password is: aK7mP2xQ
```

The output can be different every time the program runs.

For example:

```
Your generated password is: 9bX4qLm8
```

Another run could produce:

```
Your generated password is: P7nQa2Zx
```

---

## 🔄 How the Program Works

```
Import random and string
          ↓
Create a character collection
          ↓
Randomly select a character
          ↓
Repeat 8 times
          ↓
Join the characters
          ↓
Display the password
```

---

## 🧪 How to Run

1. Make sure Python 3 is installed.
2. Open the terminal inside this folder and run:

```bash
python password_generator.py
```

3. The program will generate and display an 8-character password.

---

## 📚 What I Learned

Through this small project, I explored:

- Python's `random` module
- Python's `string` module
- `random.choice()`
- `string.ascii_letters`
- `string.digits`
- `range()`
- `join()`
- Generator expressions
- f-strings
- Combining multiple Python concepts in a small program

---

## ⚠️ Important Note

This project is created for learning and demonstration purposes.

The generated password is suitable for experimenting with Python's random-selection functionality, but this simple approach should not be treated as a secure password-generation system for real-world security-sensitive applications.

Production password generators should use Python's `secrets` module, which is designed for security-sensitive random values.

---

## 🚀 Possible Improvements

This simple project could be extended by adding:

- Custom password length
- Special characters
- User-selected character types
- Multiple password generation
- Password strength indicators
- A secure implementation using Python's `secrets` module

---

## 🐍 About This Discovery

This is Day 03 of:

**100 Days, 100 Tiny Python Discoveries**

The idea is simple:

**Learn → Code → Run → Discover → Repeat**

Small programs can teach powerful programming concepts.

---

## 📌 Project Information

- **Day:** 03
- **Topic:** Password Generator
- **Language:** Python
- **Modules:** `random`, `string`
- **Difficulty:** Beginner

---

### Final folder

```text
Day_03_Password_Generator/
│
├── password_generator.py
└── README.md
```