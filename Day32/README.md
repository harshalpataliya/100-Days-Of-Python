# Day 32 - Automated Birthday Wisher

Today I worked on an automated birthday wisher project using Python.

The main goal of this project was to check a birthday CSV file, find out if someone has a birthday today, create a personalized birthday letter, and send it to their email automatically.

## What I Learned

### 1. Working with datetime

I used the `datetime` module to get today's month and day.

```python
import datetime as dt

now = dt.datetime.now()

today_day = now.day
today_month = now.month

today = (today_month, today_day)```