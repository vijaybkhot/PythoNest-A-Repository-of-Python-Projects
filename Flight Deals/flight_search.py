from datetime import timedelta

import requests
from _datetime import datetime
from flight_data import FlightData
from pprint import pprint


API_KEY = "TmDXPj6kav5X_Dz2T9AX-10mteBzq_JE"
TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.headers_KIWI = {
            "apikey": API_KEY,
            "Content-Type": 'application/json',
        }

    @staticmethod
    def get_destination_code(city_name):
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        # Data for the location API request
        location_data = {
            "term": city_name,
            "locale": "en-US",
            "location_types": "city",
        }
        headers_kiwi = {
            'apikey': API_KEY,
        }
        response_location = requests.get(url=location_endpoint, headers=headers_kiwi, params=location_data)
        location_code = response_location.json()['locations'][0]['code']
        return location_code

    @staticmethod
    def get_flight_details(origin_city_code, destination_city_code, from_time, to_time):
        date_today = datetime.now().today().strftime(f'%d/%m/%Y')
        future_date = (datetime.today() + timedelta(days=180)).strftime('%d/%m/%Y')
        search_endpoint = f"{TEQUILA_ENDPOINT}/search"
        # Data for the fight search API request
        stop_over = 0
        location_data = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 30,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "USD"
        }
        headers_kiwi = {
            'apikey': API_KEY,
        }
        response_location = requests.get(
            url=search_endpoint,
            headers=headers_kiwi,
            params=location_data)
        try:
            data = response_location.json()["data"][0]
        except IndexError:
            ##########################
            location_data["max_stopovers"] = 2
            response = requests.get(
                url=f"{TEQUILA_ENDPOINT}/v2/search",
                headers=headers_kiwi,
                params=location_data,
            )
            data = response.json()["data"][0]
            flight_data = FlightData(
                price=data['price'],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][2]["local_departure"].split("T")[0],
                stop_over=2,
                via_city=data["route"][0]["cityTo"],
            )
            print(f"{flight_data.destination_city}: ${flight_data.price}")
            return flight_data
        else:
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=datetime.utcfromtimestamp(data["route"][0]["dTime"]).strftime('%d/%m/%Y'),
                return_date=datetime.utcfromtimestamp(data["route"][1]["dTime"]).strftime('%d/%m/%Y'),
            )
            return flight_data
