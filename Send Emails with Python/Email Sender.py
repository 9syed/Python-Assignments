# You don't need to install these two libries smtplib & EmailMessage because, this package is installed with Python.
import smtplib
from email.message import EmailMessage

email = EmailMessage()
# In place of 'Sender' enter your email adderess
email['From'] = 'Sender'
# In place of 'Email Receiver' enter the email adderess of the person to who you are sending email.
email['To'] = 'Email Receiver'
# Enter email subject
email['Subject'] = 'Hello This is Python Test Email!'

with open('Text.txt', 'r') as myfile:
    content = myfile.read()
    email.set_content(content)

# Before setting up the SMTP server, we need an App password. We use the generated app password to sign in to our email account instead of using the actual password because, Our code is a less secured, Hackers can get in easily & Google doesn’t allow it.
# Learn how to create app password https://support.google.com/accounts/answer/185833?hl=en#zippy=%2Cwhy-you-may-need-an-app-password

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login('Senders Email', 'App password')
    smtp.send_message(email)
    print("Email Sent!")