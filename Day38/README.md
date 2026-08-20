# Day 38 - Workout Tracking with Google Sheets

## About

Today I learned how to work with APIs to build a real-world workout tracking application.

For today's project, I created a **Workout Tracking program** that uses the Nutritionix API to understand workout information written in natural language and then sends the workout data to a Google Spreadsheet using the Sheety API.

## What I Learned

- How to work with multiple APIs in one Python project
- How to make POST requests
- How to send request headers
- How to send JSON data in an API request
- How to work with API responses
- How to extract information from JSON responses
- How to use the Nutritionix API
- How to use the Sheety API
- How to work with Google Sheets through an API
- How to use `datetime` to get the current date and time
- How to automate data entry into a spreadsheet
- How to use environment variables to protect API credentials

## Project Workflow

The program works like this:

```text
User enters workout
        ↓
Python Program
        ↓
Nutritionix API
        ↓
Exercise Information
        ↓
Python processes the response
        ↓
Sheety API
        ↓
Google Spreadsheet 