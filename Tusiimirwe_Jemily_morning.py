
import requests
import csv
from bs4 import BeautifulSoup

url = "https://xeno-canto.org/api/2/recordings?query=sp&field=species"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    if "recordings" in data:
        species_list = list({recording["sp"] for recording in data["recordings"]})

        # Specify the file path for the CSV file
        csv_file_path = "species_list.csv"

        # Write the species_list to the CSV file
        with open(csv_file_path, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Species"])  
            writer.writerows([[species] for species in species_list])  

        print("Data saved to CSV file successfully.")

        soup = BeautifulSoup(response.text, "html.parser")
else:
    print(" Unable to fetch data from the API.")
