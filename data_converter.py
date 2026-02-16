from pathlib import Path
import json, csv


class DataConverter:
    """
    Simple class that is a data converter to convert JSON in CSV and vice versa.
    """
    def __init__(self, file) -> None:
        """Initialization of class attributes."""
        self.file = file

    def json_to_csv(self, filename: str):
        """
        Method to convert JSON in CSV file
        """
        path = "month-1-python-tools/projects/data-converter/"
        path_json = Path(f"{path}{self.file}.json") # Path of the JSON to convert
        path_csv = Path(f"{filename.lower().strip()}.csv") # Path CSV file

        try: # Check if the file exist and if we can open it
            with path_json.open(mode='r') as json_file:
                data_json = json.load(json_file)
                with path_csv.open(mode='w') as csv_file:
                    fieldnames = {key for data in data_json for key in data}
                    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(data_json)
                    return "Your CSV file is ready!", path_csv

        except FileNotFoundError as e: # If we have an error to open the JSON file
            return f"Error: {e}", None
        
         

# Tests
converter = DataConverter("test")
result, path = converter.json_to_csv("output")

print(result)
print(f"File created at: {path}")