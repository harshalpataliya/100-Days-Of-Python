# Day 30 - Password Manager (Error Handling & JSON Data)

## Overview

Today I improved my Password Manager project by adding error handling and improving the way data is stored. I learned how to handle exceptions using `try`, `except`, `else`, and `finally`. I also learned how to work with JSON files instead of storing passwords in a text file.

## What I Learned

- Understanding exceptions in Python
- Using `try`, `except`, `else`, and `finally`
- Handling `FileNotFoundError`
- Handling `KeyError`
- Raising custom exceptions
- Using `messagebox` to interact with the user
- Validating user input before saving data
- Using `messagebox.showinfo()`
- Using `messagebox.askokcancel()`
- Reading JSON files with `json.load()`
- Writing JSON files with `json.dump()`
- Updating existing JSON data
- Using dictionaries to organize and store password information
- Improving the Password Manager by saving credentials in JSON format

## Features

- Generate secure random passwords
- Save website, email, and password
- Validate empty input fields
- Display confirmation popup before saving
- Store passwords in `data.json`
- Read previously saved data
- Handle missing JSON files without crashing
- Handle missing website records safely

## Concepts Practiced

- Exception Handling
- JSON Module
- Dictionaries
- Nested Dictionaries
- File Handling
- Tkinter
- Functions
- Event Handling
- User Input Validation

## What I Found Challenging

- Understanding how `try` and `except` work together
- Knowing when to use `else` and `finally`
- Working with nested dictionaries
- Reading and updating JSON data
- Handling errors without stopping the program
- Connecting exception handling with the Password Manager

## 

Today I learned how professional applications prevent crashes by handling exceptions. I also learned why JSON is a better way to store structured data than a plain text file. This project helped me understand how to make applications more reliable, user-friendly, and organized.