# Flight Deal Finder 

## About

A Python-based Flight Deal Finder that searches for affordable flights, compares them with target prices stored in a Google Sheet, and sends notifications when a cheaper flight is found.

This project was built as the **Day 39 Capstone Project** of Angela Yu's **100 Days of Python** course.

## Features

* Search for available flights
* Find the cheapest flight
* Compare flight prices with target prices
* Search for direct flights
* Search for indirect flights when necessary
* Read destination data from Google Sheets
* Update the lowest price in the spreadsheet
* Send WhatsApp notifications
* Send email notifications
* Use API caching to reduce unnecessary requests

## Technologies Used

* Python
* Requests
* SerpAPI
* Sheety API
* Google Sheets
* Twilio
* Requests Cache
* python-dotenv

## Project Structure

* `main.py` – Controls the complete application workflow
* `data_manager.py` – Handles Google Sheet operations
* `flight_search.py` – Searches for flights using SerpAPI
* `flight_data.py` – Finds the cheapest flight
* `notification_manager.py` – Sends WhatsApp and email notifications
* `.env` – Stores API credentials securely

## How It Works

The program first retrieves destination information and target prices from a Google Sheet.

It then searches for flights from the origin airport to each destination using the SerpAPI Google Flights engine.

The cheapest available flight is identified and compared with the target price stored in the spreadsheet.

If a cheaper flight is found, the program updates the spreadsheet and sends a notification containing the flight details.

If no direct flight is available, the program also searches for indirect flights.

## Python Concepts Learned

* Object-Oriented Programming
* Classes and Objects
* Functions and Methods
* Dictionaries and Lists
* List Comprehension
* HTTP GET and PUT Requests
* APIs
* JSON
* API Authentication
* Environment Variables
* HTTP Status Codes
* Error Handling
* `datetime`
* `timedelta`
* `strftime()`
* Request Caching

## Key Learning

This project helped me understand how multiple classes, APIs, and Python concepts can be combined to create a real-world application.

The project separates different responsibilities into different classes:

* **DataManager** – Spreadsheet operations
* **FlightSearch** – Flight searching
* **FlightData** – Flight data processing
* **NotificationManager** – Notifications
* **main.py** – Connects everything together
