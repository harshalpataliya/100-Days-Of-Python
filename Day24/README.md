# Day 24 - Files, Directories & Paths 

##  Topics Learned

- Reading text files using `open()`
- Writing to text files
- File modes (`r`, `w`, `a`)
- The `with` keyword for automatic file handling
- Absolute vs Relative file paths
- Working with directories
- String replacement using `replace()`
- Removing whitespace using `strip()`

## Projects

### 1. Reading & Writing Files
- Read text from a file using `read()`
- Write new content to a file
- Append content using append mode (`a`)

### 2. File Path Practice
- Worked with absolute file paths
- Learned how relative paths work
- Understood how the current working directory affects file access

### 3. Mail Merge Project 
Built a Mail Merge program that:
- Reads a list of names from a text file
- Reads a letter template
- Replaces the placeholder (`[name]`) with each person's name
- Generates personalized letters automatically
- Saves each letter in the output folder

##  Concepts

- `open()`
- `read()`
- `readlines()`
- `write()`
- `replace()`
- `strip()`
- `with open()`
- Relative Paths
- Absolute Paths

## Project Structure

Day24/
│
├── Input/
│   ├── Letters/
│   │   └── starting_letter.txt
│   └── Names/
│       └── invited_names.txt
│
├── Output/
│   └── ReadyToSend/
│
└── main.py


## What I Learned

- Safely opening and closing files using the `with` statement.
- Reading and writing text files in Python.
- Understanding the difference between absolute and relative file paths.
- Automating repetitive tasks by generating personalized files.
- Applying string manipulation with `replace()` and `strip()`.
