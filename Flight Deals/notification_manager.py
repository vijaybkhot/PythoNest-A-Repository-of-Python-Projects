import requests
from twilio.rest import Client
import smtplib

# Twilio API credentials
account_sid = "AC972ae7b4c92e28a1e2807813235f2550"
auth_token = "6bf288fde82ba2087dae1cee73b6856a"
client_twilio = Client(account_sid, auth_token)
client_twilio_whatsapp = Client(account_sid, auth_token)

# E-mail credentials



class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client_twilio_whatsapp = Client(account_sid, auth_token)
        self.client_twilio = Client(account_sid, auth_token)
        self.my_email = "vijay.b.khot.01@gmail.com"
        self.my_password = "xihh ijio vdpv keow"

    def send_message(self, message):
        # Send SMS using Twilio
        message_twilio = self.client_twilio.messages.create(
            body=message,
            from_='+1(866) 699-4459',
            to='+15512414753'
        )
        whatsapp_message_twilio = self.client_twilio_whatsapp.messages.create(
            body=message,
            from_='whatsapp:+14155238886',
            to='whatsapp:+917276481813'
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
