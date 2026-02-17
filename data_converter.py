from pathlib import Path
import json, csv


class DataConverter:
    """
    Simple class that is a data converter to convert JSON in CSV and vice versa.
    """
    def __init__(self, file: str, path: str="") -> None:
        """Initialization of class attributes."""
        self.file = file
        self.path = path

    def json_to_csv(self, filename: str, path: str="") -> str:
        """
        Method to convert JSON in CSV file
        """
        path_json = Path(f"{self.path}{self.file}.json") # Path of the JSON to convert
        path_csv = Path(f"{path}{filename.lower().strip()}.csv") # Path CSV file

        try: # Check if the file exist and if we can open it
            with path_json.open(mode='r') as json_file:
                data_json = json.load(json_file)
                with path_csv.open(mode='w') as csv_file:
                    fieldnames = {key for data in data_json for key in data}
                    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(data_json)
                    return f"Find your CSV file here: {path_csv}"

        except FileNotFoundError as e: # If we have an error to open the JSON file
            return f"Error: {e}"
        
    
    def csv_to_json(self, filename: str, path: str="") -> str:
        """
        Method to convert CSV in JSON file
        """
        path_csv = Path(f"{self.path}{self.file}.csv") # Path CSV file
        path_json = Path(f"{path}{filename.lower().strip()}.json") # Path of the JSON to convert

        try:
            with path_csv.open(mode='r') as csv_file:
                csv_reader = list(csv.DictReader(csv_file))
                with path_json.open(mode='w') as json_file:
                    json.dump(csv_reader, fp=json_file, indent=2)
                    return f"Find your JSON file here: {path_json}"
        
        except FileNotFoundError as e:
            return f"Error: {e}"