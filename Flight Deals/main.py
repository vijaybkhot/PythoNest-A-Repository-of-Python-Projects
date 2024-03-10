# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.
from datetime import timedelta
from _datetime import datetime

from notification_manager import NotificationManager
from data_manager import DataManager
from flight_search import FlightSearch

import requests

API_KEY = "TEQUILA API KEY"
TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

ORIGIN_CITY_IATA = "NYC"

# sheety_data = data_manager.get_sheety_data()

sheety_data = {'prices': [{'city': 'Paris', 'iataCode': 'PAR', 'lowestPrice': 54, 'id': 2},
                          {'city': 'Berlin', 'iataCode': 'BER', 'lowestPrice': 42, 'id': 3},
                          {'city': 'Tokyo', 'iataCode': 'TYO', 'lowestPrice': 485, 'id': 4},
                          {'city': 'Sydney', 'iataCode': 'SYD', 'lowestPrice': 551, 'id': 5},
                          {'city': 'Istanbul', 'iataCode': 'IST', 'lowestPrice': 95, 'id': 6},
                          {'city': 'Kuala Lumpur', 'iataCode': 'KUL', 'lowestPrice': 414, 'id': 7},
                          {'city': 'San Francisco', 'iataCode': 'SFO', 'lowestPrice': 260, 'id': 8},
                          {'city': 'Cape Town', 'iataCode': 'CPT', 'lowestPrice': 378, 'id': 9},
                          {'city': 'Mumbai', 'iataCode': 'BOM', 'lowestPrice': 2000, 'id': 10},
                          {'city': 'Bali ', 'iataCode': 'DPS', 'lowestPrice': 1002, 'id': 11},
                          ]}

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

stop_over = 0
for item in range(len(sheety_data['prices'])):
    city = sheety_data['prices'][item]['iataCode']
    flight = flight_search.get_flight_details(
        ORIGIN_CITY_IATA,
        city,
        from_time=tomorrow,
        to_time=six_month_from_today,
    )

    if flight.price < sheety_data['prices'][item]['lowestPrice']:
        notification_manager.send_message(
            message=f"Low price alert! Only ${flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
                    f"Flight has {flight.stop_overs} stop over/overs, via {flight.via_city} City"
        )

        notification_manager.send_email(
            subject="Low Price Alert",
            message=f"Low price alert! Only ${flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
                    f"Flight has {flight.stop_overs} stop over/overs, via {flight.via_city}",
            to_email=data_manager.get_emails()
        )
        data_manager.update_price(
            flight_price=flight.price,
            departure_date=flight.out_date,
            return_date=flight.return_date,
            sheety_data_row=sheety_data['prices'][item],
        )
