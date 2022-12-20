import os
import smtplib
from email.message import EmailMessage
import ssl
from dotenv import load_dotenv


def send_email(course, section, seats):
    load_dotenv()
    email_sender = os.environ.get('EMAIL_USERNAME')
    email_password = os.environ.get('EMAIL_PASSWORD')

    if seats <= 0:
        subject = course + ' Section ' + section + ' is Now Empty'
        body = 'unfortunately, ' + course + ' Section ' + section + ' is empty. We will keep you updated if any seats become avaialble.'
    elif seats == 1:
        subject = course + ' Section ' + section + ' Has a Seat Availible!'
        body = course + ' Section ' + section + ' has ' + str(seats) + ' seat availible! You can go to https://classsearch.nd.edu to register for this class.'
    else:
        subject = course + ' Section ' + section + ' Has Seats Availible!'
        body = course + ' Section ' + section + ' has ' + str(seats) + ' seats availible! You can go to https://classsearch.nd.edu to register for this class.'
    
    e = EmailMessage()
    e['From'] = email_sender
    e['To'] = email_sender
    e['Subject'] = subject
    e.set_content(body)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_sender, e.as_string())
