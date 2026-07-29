# Day 27 - Tkinter GUI and Function Arguments

## What I Learned

Today I learned the basics of creating GUI applications using Python's Tkinter module. I also learned about `*args` and `**kwargs` and how they are used in Python functions.

### Tkinter

- Imported the Tkinter module using `from tkinter import *`
- Created a window using the `Tk()` class
- Set the window title using `title()`
- Set the minimum window size using `minsize()`
- Created labels using the `Label` class
- Created buttons using the `Button` class
- Created text input fields using the `Entry` class
- Displayed widgets using both `pack()` and `grid()`
- Learned that `pack()` and `grid()` should not be used together in the same container
- Used the `config()` method to update widget properties after they were created
- Connected a button to a function using the `command` parameter
- Retrieved user input using the `get()` method
- Built a simple Miles to Kilometers Converter GUI application

### *args

- Learned that `*args` allows a function to accept any number of positional arguments
- Understood that `args` is stored as a tuple
- Used a loop to iterate through all arguments
- Calculated the total by adding each value inside the loop

### **kwargs

- Learned that `**kwargs` allows a function to accept any number of keyword arguments
- Understood that `kwargs` is stored as a dictionary
- Accessed values using dictionary keys
- Learned how `kwargs.get()` can safely retrieve values without causing errors

### Tkinter Classes

- Learned that widgets in Tkinter are created from classes
- Created objects from classes such as:
  - Tk
  - Label
  - Button
  - Entry
- Learned that each widget is an object and its properties can be modified later using methods like `config()`

## Project

### Miles to Kilometers Converter

Created a GUI application that:

- Takes miles as input from the user
- Converts miles into kilometers
- Displays the converted value when the Calculate button is clicked

## Concepts

- GUI Programming
- Event Handling
- Functions
- Button Commands
- Object-Oriented Programming Basics
- Tkinter Widgets
- User Input
- Updating Widget Properties
- *args
- **kwargs

## Status

Day 27 Completed