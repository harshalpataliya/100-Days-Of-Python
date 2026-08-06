# Day 31 - Flash Card App (Capstone Project)

## Overview

Today I built a Flash Card application using Python and Tkinter. This project helped me combine many concepts that I learned in previous lessons, such as Tkinter, Pandas, CSV files, timers, random module, and file handling. The application displays French words, flips the card after a few seconds to show the English translation, and helps users learn vocabulary interactively.

## What I Learned

- Building a complete Tkinter application
- Working with the `Canvas` widget
- Displaying and changing images using `PhotoImage`
- Creating and updating Canvas text
- Reading CSV files using Pandas
- Converting a DataFrame into a list of dictionaries
- Selecting random data using `random.choice()`
- Using global variables when required
- Using `window.after()` to schedule events
- Updating Canvas items using `canvas.itemconfig()`
- Switching between front and back card images
- Removing learned words from the dataset
- Saving learning progress using CSV files
- Organizing a project using functions and sections

## Features

- Displays a random French word
- Automatically flips the card after a few seconds
- Shows the English translation
- "Known" button removes the word from the learning list
- "Unknown" button keeps the word for future practice
- Saves learning progress so completed words do not appear again
- Simple and interactive graphical user interface

## Concepts Practiced

- Tkinter GUI Development
- Canvas Widget
- Event Handling
- Timers (`window.after()`)
- Functions
- Random Module
- Pandas
- CSV File Handling
- Dictionaries
- Lists
- File Management


## Challenges Faced

- Understanding how Canvas differs from Label
- Positioning widgets correctly using `grid()`
- Updating existing Canvas text instead of creating new text
- Loading and converting CSV data using Pandas
- Managing random flash cards
- Understanding the purpose of `window.after()`
- Updating the flash card after a delay
- Saving the remaining words after learning new vocabulary

## What I Learned from This Project

This was my second capstone project in the course. It helped me combine concepts from previous days instead of learning completely new topics. I understood how different Python modules work together to create a real desktop application. I also became more comfortable with planning a project by breaking it into smaller functions.
