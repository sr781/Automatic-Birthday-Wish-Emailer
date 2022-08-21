import pandas
import datetime as dt
import random
import smtplib
my_email = "sulav1080@outlook.com"  # The email and password for the host (Outlook)
password = "Orchid123!"  # These details will not work, please create your own Outlook account
now = dt.datetime.now()  # use the datetime class (dt) of the datetime module to get the time now
birthday_info = pandas.read_csv("birthdays.csv")  # Read the csv file which contains birthday date and user information into a data frame


for a in range(0, len(birthday_info)):  # Loops through the data frane
    month = birthday_info.month[a]
    day = birthday_info.day[a]
    if now.month == month and now.day == day:  # If the day and month from the datetime module matches the day and month from the data frame, this if statement is activated
        with open(f"letter_templates/letter_{random.randint(1,3)}.txt", "r") as send_pending_letter:  # Opens a random letter template (three to choose from)
            contents = send_pending_letter.read()  # Reads file into a string
            contents = contents.replace("[NAME],", f"{birthday_info.name[a]}")  # Replaces "[NAME]," in the file with the recipients name
            print(contents)
        with smtplib.SMTP("outlook.office365.com") as connection:  # Using the smtplib library to send emails using the simple mail transfer protocol
            connection.starttls()  # Encrypts connection
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=f"{birthday_info.email[a]}",
                                msg=f"Subject:Birthday Wishes for {birthday_info.name[a]}! \n\n {contents}")  # This function








