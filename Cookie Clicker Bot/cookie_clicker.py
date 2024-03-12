"""
This script automates clicking the cookie and buying items in the store in the Cookie Clicker game.
It uses the Selenium WebDriver to interact with the browser.

Instructions:
- Make sure you have the Selenium library installed: pip install selenium
- Download the Chrome WebDriver from https://sites.google.com/a/chromium.org/chromedriver/downloads
  and place it in the same directory as this script or provide the path to it.
- Run the script and watch it play Cookie Clicker for you!

"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("start-maximized")

# Create and configure chrome webdriver
driver = webdriver.Chrome(options=chrome_options)

# Navigate to cookie clicker webpage
driver.get("https://orteil.dashnet.org/experiments/cookie/")

# Find the cookie element by its ID
cookie = driver.find_element(By.ID, value="cookie")

# Set the initial time for 5 seconds interval and 5 minutes total
five_sec = time.time() + 5
five_min = time.time() + 300

# Continuous loop for clicking cookie and checking store
while True:
    # Click the cookie
    cookie.click()

    # Check if 5 seconds have passed
    if time.time() > five_sec:
        # Find all store items that are not grayed out
        store = driver.find_elements(By.CSS_SELECTOR, "#store > div:not(.grayed)")
        if store:
            # Click the last non-grayed out store item
            store[-1].click()
            # Update the 5 seconds interval time
            five_sec = time.time() + 5

    # Check if 5 minutes have passed
    if time.time() > five_min:
        # Find the CPS element and print its text
        cps = driver.find_element(By.ID, value="cps")
        if cps:
            print(cps.text)
        # Exit the loop after printing CPS
        break
