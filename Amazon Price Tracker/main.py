"""
This script fetches the price of a product from Amazon and compares it to a target price.
If the current price is less than or equal to the target price, it sends an email notification using the Notification class.

The script uses BeautifulSoup for parsing HTML content and requests for sending HTTP requests.

Before running the script, ensure that the Notification class is implemented in a separate module.

"""
# Import necessary libraries
from bs4 import BeautifulSoup
import requests
import lxml
from notification import Notification

# Initialize Notification object for sending notifications
notification = Notification()

# Define the target price and the URL of the product
TARGET_PRICE = 8.00
PRODUCT_URL = "https://www.amazon.com/Logitech-Wireless-Receiver-12-Months-Ambidextrous/dp/B074L9L5KZ/ref=sr_1_10?crid=OM3RPAOMR19S&dib=eyJ2IjoiMSJ9.AhB9TFksy_6f4mUIvqSwmrt6qMWjY0fZH2qP_V_6LRXzrq8FtdIAQZJXPc429pacbXOx9Nu_RQ6pa48Y0IQQo9UjOMsKkgVCUUQ1IbvysBsrByuYg0s_oCirkJieS9eW-shzOTDMJoWsGaRfe_E8DFTg5lYgEgNZDUF0mMtAiXlMGqp7naEXu1kGmUfWUOLSIfwjBmX6fK7YkM_cd3GikW5l8kQrdqaTGxAoHmO6HL0.FekBqcrWl7X-pWBjbhjjTg7nVOpO2RVBQ8DqutNBTYw&dib_tag=se&keywords=mouse%2Bbluetooth&qid=1710071993&sprefix=mouse%2Bbluetooth%2Caps%2C94&sr=8-10&th=1"

# Define headers for the HTTP request
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7'
}

# Send HTTP GET request to the product URL
response = requests.get(url=PRODUCT_URL, headers=headers)

# Parse the HTML content of the response using BeautifulSoup
soup = BeautifulSoup(response.text, "lxml")

# Extract the price of the product from the parsed HTML
price = float(soup.find(name="span", class_='aok-offscreen').text.split("$")[1])

# Extract the title of the product from the parsed HTML
product_title = soup.find(name='span', id='productTitle').text.strip()

# Check if the current price is less than or equal to the target price
if price <= TARGET_PRICE:
    # If the condition is met, send an email notification
    notification.send_email(product_title=product_title, target_price=TARGET_PRICE, price=price)
    print("Price Update")
