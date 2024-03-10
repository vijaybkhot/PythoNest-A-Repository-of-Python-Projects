import requests

# Pixela API endpoint for user registration
pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "vijaykhot"
TOKEN = "hiasakn123#@$BDJH8&bhA"


class HabitTracker:
    def __init__(self):
        """
        Initialize the HabitTracker class with user parameters, headers, graph configuration,
        and endpoint for adding pixels.
        """
        self.user_params = {
            "token": TOKEN,
            "username": USERNAME,
            "agreeTermsOfService": "yes",
            "notMinor": "yes",
        }
        self.headers = {
            "X-USER-TOKEN": TOKEN
        }
        self.graph_config = {
            "id": "graph2",
            "name": "Study Graph",
            "unit": "hours",
            "type": "float",
            "color": "momiji",
        }
        self.add_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{self.graph_config['id']}"

    def add_pixel(self, date, quantity):
        """
        Add a pixel to the graph for the given date and quantity.

        Args:
        - date (str): The date in YYYYMMDD format.
        - quantity (int): The quantity to add to the graph for the given date.
        """
        add_pixel_config = {
            "date": date,
            "quantity": f"{quantity}",
        }
        response = requests.post(url=self.add_pixel_endpoint, json=add_pixel_config, headers=self.headers)
        response.raise_for_status()
        print(response.text)

    def get_pixel_info(self, date):
        """
        Get information about a pixel for the given date.

        Args:
        - date (str): The date in YYYYMMDD format.
        """
        get_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{date}"
        response_get = requests.get(url=get_pixel_endpoint, headers=self.headers)
        response_get.raise_for_status()
        json_data = response_get.json()
        print(json_data)
