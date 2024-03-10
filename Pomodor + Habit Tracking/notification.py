import smtplib


class Notification:
    def __init__(self):
        """
        Initialize the Notification class with the sender's email and password.
        """
        self.my_email = "vijay.b.khot.01@gmail.com"
        self.my_password = "xihh ijio vdpv keow"

    def send_email(self, date, quantity, signal):
        """
        Send an email notification about the study progress.

        Args:
        - date (str): The date of the study progress.
        - quantity (float): The quantity of study hours.
        """
        if signal == 1:
            message = f"Subject:Last Study Update on your Habit Tracking\n\n" \
                      f"On {date}, you studied for {quantity} hours. Keep up the good work!"
        else:
            message = f"Subject:Welcome to Habit Tracking\n\n" \
                      f"Congratulations on starting your work on {date}. All the best!"

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=self.my_email, password=self.my_password)
            connection.sendmail(
                from_addr=self.my_email,
                to_addrs="vijaysinh.khot@gmail.com",
                msg=message
            )
