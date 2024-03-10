import requests
from pprint import pprint
from flight_search import FlightSearch
from datetime import datetime, timedelta

GOOGLE_SHEET_NAME_PRICES = "price"
GOOGLE_SHEET_NAME_USERS = "user"
SHEETY_API_PRICES = "https://api.sheety.co/33ada152d77d41a689f79cd8bd4c7262/flightDeals/prices"
SHEETY_API_USERS = "https://api.sheety.co/33ada152d77d41a689f79cd8bd4c7262/flightDeals/users"


class DataManager:

    def __init__(self):
        # This class is responsible for talking to the Google Sheet.
        # Google Sheet details
        # Sheety API endpoint and headers
        self.bearer = "#Your bearer id"
        self.headers_sheety_bearer = {
            "Authorization": f"Bearer {self.bearer}",
            "Content-Type": 'application/json',
        }

    def update_sheet_data(self, sheety_data, new_price):
        # sheety_input = {}
        for row_number in range(len(sheety_data)):
            sheety_input = {
                GOOGLE_SHEET_NAME_PRICES: {
                    "city": sheety_data[row_number]['city'],
                    "iataCode": sheety_data[row_number]['iataCode'],
                    "lowestPrice": new_price,
                }
            }
            # Making a PUT request to Sheety API
            if new_price < sheety_data[row_number]['lowestPrice']:
                response_sheety = requests.put(url=f"{SHEETY_API_PRICES}/{sheety_data[row_number]['id']}",
                                               json=sheety_input,
                                               headers=self.headers_sheety_bearer)
                # Check if the request was successful
                if response_sheety.status_code == 200:
                    sheety_text = response_sheety.json()
                    print(sheety_text)
                else:
                    print(f"Error: Unable to update sheet data. Status code: {response_sheety.status_code}")

    def get_sheety_data(self):
        # Making a GET request to Sheety API
        response_sheety = requests.get(url=f"{SHEETY_API_PRICES}",
                                       headers=self.headers_sheety_bearer)
        # Check if the request was successful
        if response_sheety.status_code == 200:
            sheety_json = response_sheety.json()
            print(sheety_json)
            return sheety_json

        else:
            print(f"Error: Unable to update sheet data. Status code: {response_sheety.status_code}")

    # 6. In the DataManager Class make a PUT request and use the row id  from sheet_data
    # to update the Google Sheet with the IATA codes. (Do this using code).
    def update_destination_codes(self, sheety_data):
        for city in sheety_data['prices']:
            new_data = {
                "price": {
                    "iataCode": FlightSearch.get_destination_code(city['city'])
                }
            }
            response = requests.put(
                url=f"{SHEETY_API_PRICES}/{city['id']}",
                json=new_data
            )
            print(response.text)

    def update_price(self, flight_price, departure_date, return_date, sheety_data_row):
        date = datetime.now() + timedelta(days=1)
        new_data = {
            "price": {
                "lowestPrice": flight_price,
                "date": date.strftime("%d/%m/%Y"),
                "flightDepartureDate": departure_date,
                "flightReturnDate": return_date,
                }
            }
        response = requests.put(
            url=f"{SHEETY_API_PRICES}/{sheety_data_row['id']}",
            json=new_data
        )
        print(response.text)

    def get_emails(self):
        # Making a GET request to Sheety API
        response_emails = requests.get(url=f"{SHEETY_API_USERS}",
                                       headers=self.headers_sheety_bearer)
        # Check if the request was successful
        if response_emails.status_code == 200:
            sheety_json = response_emails.json()
            emails = [item['email'] for item in sheety_json['users']]
            return emails
            #{'users': [{'firstName': 'vijay', 'lastName': 'khot', 'email': 'vijay111991@gmail.com', 'id': 2}]}

        else:
            print(f"Error: Unable to get sheet data. Status code: {response_emails.status_code}")


