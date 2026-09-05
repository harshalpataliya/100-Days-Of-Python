<!-- .env
SMTP_ADDRESS="smtp.gmail.com"
EMAIL_ADDRESS="your_email@email.com"
EMAIL_PASSWORD="your app password" -->

The above code is for .env folder to make privacy.


#  Day 47 – Amazon Price Tracker

## About

In this project, I built an **Amazon Price Tracker** using Python.

The program checks the price of a product on Amazon and compares it with a target price. If the product price drops below the target price, the program can send an **email notification** to inform the user that the product is available at a lower price.

This project combines:

- Web Scraping
- HTTP Requests
- Beautiful Soup
- HTML Parsing
- Finding HTML Elements
- Extracting Product Information
- Price Comparison
- Email Automation
- SMTP
- Environment Variables
- Exception Handling

---

#  Project Goal

The main goal of this project is to automatically monitor the price of an Amazon product.

The basic workflow is:

```text
Amazon Product Page
        ↓
Send HTTP Request
        ↓
Get HTML
        ↓
Beautiful Soup
        ↓
Extract Product Price
        ↓
Compare With Target Price
        ↓
Price Is Low Enough?
      ↙       ↘
    YES        NO
     ↓          ↓
Send Email    Do Nothing