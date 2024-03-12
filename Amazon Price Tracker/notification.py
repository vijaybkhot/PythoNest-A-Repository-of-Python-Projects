import smtplib

class Notification:
    def __init__(self):
        """
        Initialize the Notification class with the sender's email and password.
        """
        self.my_email = "User Email"
        self.my_password = "Password"

    def send_email(self, product_title, target_price, price):
        """
        Send an email notification when the price of the product drops below the target price.

        Args:
        - date (str): The date of the study progress.
        - quantity (float): The quantity of study hours.
        """
        message = f"Subject:${price} for {product_title}!!\n\n" \
                  f"The price of the product {product_title} has dropped below ${target_price} The price of the product is ${price}!"

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=self.my_email, password=self.my_password)
            connection.sendmail(
                from_addr=self.my_email,
                to_addrs="receivers email",
                msg=message
            )
