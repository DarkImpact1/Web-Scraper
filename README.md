# Web-Scraper
Mobiles Under 30k
This is a Python script that scrapes data from the Flipkart website and writes it to a CSV file.
The script fetches the details of mobile phones under 30,000 INR and extracts their name, price, exchange offer, RAM & ROM, processor, display, camera, battery, and warranty.

Libraries used
The script uses the following Python libraries:

requests: to make HTTP requests to the website.
beautifulsoup4: to parse the HTML content of the website.
csv: to write the data to a CSV file.
How to run the script
To run this script, follow these steps:

Clone this repository.
Install the required libraries (requests and beautifulsoup4) using pip.
Run the script using python mobiles_under_30k.py. The data will be written to a CSV file named mobiles_under_30k.csv.
Output
The CSV file mobiles_under_30k.csv will have the following columns:

Mobile Name
Price
Exchange Offer
RAM & ROM
Processor
Display
Camera
Battery
Warranty (if available)
The data will be extracted from the Flipkart website and written to this file. The file will be created in the same directory as the script.

Note
This script was last tested on September 2021. The website structure may have changed since then, which may cause the script to fail. 
In such a case, the script may need to be updated to work with the current website structure.
