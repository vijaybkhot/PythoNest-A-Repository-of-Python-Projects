import json
import os
from datetime import datetime


class DataUpdate:
    def __init__(self):
        """Initialize the DataUpdate class with the path to the data file."""
        self.data_file_path = "data.json"

    def update_data_file(self):
        """
        Update the data file with the current date and quantity.
        If an entry for the current date already exists, update the quantity.
        Otherwise, add a new entry for the current date.
        Return the latest entry.
        """
        # Load data from the file
        if os.path.exists(self.data_file_path):
            with open(self.data_file_path, "r") as file:
                file_content = file.read()
                if file_content.strip() == "":
                    data = []
                else:
                    data = json.loads(file_content)
        else:
            data = []

        current_date = datetime.today().strftime("%Y-%m-%d")

        # Check if there is an entry for the current date
        existing_entry_index = next((index for index, item in enumerate(data) if item["date"] == current_date), None)

        if existing_entry_index is not None:
            # If there is an entry for the current date, update the quantity
            data[existing_entry_index]["quantity"] += 0.5
        else:
            # If there is no entry for the current date, add a new entry
            new_entry = {"date": current_date, "quantity": 0.5}
            data.append(new_entry)

        # Save the updated data back to the file
        with open(self.data_file_path, "w") as file:
            json.dump(data, file)

        # Return the latest entry
        sorted_data = sorted(data, key=lambda x: x["date"], reverse=True)
        if sorted_data:
            return sorted_data
        else:
            return None



