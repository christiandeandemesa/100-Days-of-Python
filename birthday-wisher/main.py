from datetime import datetime
import pandas
import random
import smtplib

MY_EMAIL = "c53539588@gmail.com"
PASSWORD="dlrlbtrfwrcwkqye"

today = datetime.now()
today_tuple = (today.month, today.day)
data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    # Creates a connection to the email provider.
    # Using the with keyword closes the connection.
    with smtplib.SMTP("smtp.gmail.com") as connection:
        # Encrypts the email while in transit.
        connection.starttls()
        # Logs into the sender's email with their password
        connection.login(MY_EMAIL, PASSWORD)
        # Creates a connection between the sender and receiver's emails.
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=birthday_person.email, msg=f"Subject:Happy Birthday\n\n{contents}")