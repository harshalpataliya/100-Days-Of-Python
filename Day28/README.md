# Day 28 - Pomodoro Timer

## What I Learned

Today I built my first complete GUI application using Tkinter by creating a Pomodoro Timer. This project helped me understand how to update the GUI dynamically and schedule tasks using Tkinter.

### Tkinter

- Created a GUI application using Tkinter.
- Used the `Canvas` widget to display images and text.
- Learned how to use `PhotoImage` to display images.
- Used `Label` widgets to display headings and check marks.
- Used `Button` widgets with the `command` parameter to execute functions.
- Organized widgets using the `grid()` geometry manager.
- Updated widget properties using the `config()` method.

### Tkinter Methods

- Learned how to use the `after()` method to schedule a function after a specific amount of time.
- Used `after_cancel()` to stop a scheduled timer.
- Used `mainloop()` to keep the application running.
- Used `config()` to update labels and canvas text while the program was running.

### Countdown Timer

- Created a countdown timer that updates every second.
- Converted total seconds into minutes and seconds.
- Formatted the timer display using f-strings.
- Displayed time in `MM:SS` format.

### Functions

- Created separate functions for:
  - Starting the timer
  - Resetting the timer
  - Counting down
- Used global variables where necessary to keep track of repetitions and timer state.

### Pomodoro Technique

Learned how the Pomodoro Technique works:

- 25 minutes of focused work
- 5 minutes short break
- 25 minutes of focused work
- 5 minutes short break
- After four work sessions, take a 20-minute long break

### Logic

- Used conditional statements to determine:
  - Work session
  - Short break
  - Long break
- Updated the title label depending on the current session.
- Displayed check marks after completing work sessions.

## Project
### Pomodoro Timer

Built a productivity timer that:

- Starts a work session
- Automatically switches to break sessions
- Displays a countdown timer
- Shows completed work sessions using check marks
- Allows the timer to be reset at any time


- Tkinter GUI
- Canvas
- PhotoImage
- Labels
- Buttons
- Grid Layout
- Event Handling
- Countdown Timer
- after()
- after_cancel()
- Global Variables
- Functions
- Conditional Statements
- Time Conversion
- Pomodoro Technique

