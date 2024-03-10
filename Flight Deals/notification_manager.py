import requests
from twilio.rest import Client
import smtplib

# Twilio API credentials
account_sid = "TWILIO SID"
auth_token = "TWILIO AUTH TOKEN"
client_twilio = Client(account_sid, auth_token)
client_twilio_whatsapp = Client(account_sid, auth_token)

# E-mail credentials



class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client_twilio_whatsapp = Client(account_sid, auth_token)
        self.client_twilio = Client(account_sid, auth_token)
        self.my_email = "vijay.b.khot.01@gmail.com"
        self.my_password = "MY PASSWORD"

    def send_message(self, message):
        # Send SMS using Twilio
        message_twilio = self.client_twilio.messages.create(
            body=message,
            from_='+text number sender',
            to='text number receiver'
        )
        whatsapp_message_twilio = self.client_twilio_whatsapp.messages.create(
            body=message,
            from_='whatsapp number sender',
            to='whatsapp number receiver'
        )

    def send_email(self, subject, message, to_email):
        # Send email using SMTP
        for email in to_email:
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=self.my_email, password=self.my_password)
                connection.sendmail(
                    from_addr=self.my_email,
                    to_addrs=email,
                    msg=f"Subject: {subject}\n\n{message}"
                )
