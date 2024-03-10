Project Name: Flight Club Project

Description: The Flight Club Project is a Python program that helps users find low-priced flights from a specified origin city to various destinations. It utilizes the Tequila Flight Search API to gather flight information and Sheety API to manage data stored in Google Sheets. The program sends notifications via SMS and email when it finds flights that match or are below a specified price threshold.

Key Features:

Allows users to specify the origin city and a list of destinations with their corresponding lowest price thresholds.
Utilizes the Tequila Flight Search API to retrieve flight details such as price, origin city, origin airport, destination city, destination airport, departure date, return date, and number of stopovers.
Checks if the price of a flight is below the specified threshold for each destination and notifies users if a low-priced flight is found.
Sends notifications via SMS using the Twilio API and via email using the SMTP protocol.
Updates the lowest price for each destination in the Google Sheet if a lower-priced flight is found.
Supports multiple destinations and can be configured to run periodically to check for new low-priced flights.

Technologies Used:

Python
Tequila Flight Search API
Sheety API
Twilio API
SMTP protocol for sending emails
Google Sheets for storing destination information and lowest prices

How It Works:

Retrieves destination information and lowest price thresholds from a Google Sheet using the Sheety API.
Uses the Tequila Flight Search API to find flights from the specified origin city to each destination.
Compares the price of each flight with the lowest price threshold for that destination.
Sends notifications via SMS and email if a low-priced flight is found, and updates the Google Sheet with the new lowest price if applicable.



Future Enhancements:

Adding more customization options for users, such as specifying preferred airlines or travel dates.
Enhancing the notification system to provide more detailed information about the flights.
Implementing a user interface for easier interaction and configuration.
Adding support for more destinations and origin cities.
Improving error handling and logging for better reliability and debugging.

