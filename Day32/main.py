import datetime as dt
import pandas
import random
import smtplib

USER = "onlypcgame08@gmail.com"
PASSWORD = "APP PASSWORD"


now = dt.datetime.now()
today_day = now.day
today_month = now.month
today = (today_month, today_day)

data = pandas.read_csv('birthdays.csv')
birthday_dict = { (data_row.month, data_row.day): data_row for index, data_row in data.iterrows()}

random_letter = random.randint(1,3)
letter_path = f"letter_templates/letter_{random_letter}.txt"

with open(letter_path, "r") as letter_file:
    letter = letter_file.read()

    if today in birthday_dict:
        birthday_person = birthday_dict[today]

        name = birthday_person["name"]

        letter = letter.replace("[NAME]", name)

    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=USER, password=PASSWORD)
        connection.sendmail(from_addr=USER,to_addrs="reciever gmail",msg=f"Subject:Ladleee Ghap Ghap Meow\n\n{letter}")





