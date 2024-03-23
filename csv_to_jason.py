import csv
import json

csv_file_path = "reservation_report.csv"
json_file_path = "reservation_report.json"

# Define the function to convert CSV to JSON
def convert_csv_to_json(csv_file_path, json_file_path):
    """
    Convert a CSV file to a JSON file.

    Parameters:
    csv_file_path (str): The file path of the CSV input.
    json_file_path (str): The file path for the JSON output.
    """
    # Initialize an empty list to store the CSV rows as dictionaries
    data = []

    try:
        # Open the CSV file for reading
        with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
            # Use DictReader to read the CSV into a dictionary
            csv_reader = csv.DictReader(csv_file)

            # Loop through the rows in the CSV
            for row in csv_reader:
                # Append each row dictionary to the data list
                data.append(row)

        # Open the JSON file for writing
        with open(json_file_path, mode='w', encoding='utf-8') as json_file:
            # Write the data list as JSON to the file, formatted with indentation for readability
            json.dump(data, json_file, indent=4)

        # Indicate success
        print(f"CSV has been successfully converted to JSON and saved to '{json_file_path}'")

    except Exception as e:
        # Print any error that occurs during the file processing
        print(f"An error occurred: {e}")

# Uncomment the lines below and replace 'input.csv' and 'output.json' with your actual file paths
# csv_file_path = 'input.csv'
# json_file_path = 'output.json'
convert_csv_to_json(csv_file_path, json_file_path)
