'''
Scrapes timezones with city names from zeitverschiebung.net.
'''

import requests
from bs4 import BeautifulSoup
import json
from CONSTANTS import SCRAPED_TIMEZONES_CITIES_JSON

# URL of the website
url = 'https://www.zeitverschiebung.net/en/all-time-zones.html'

# Make a GET request to fetch the raw HTML content
response = requests.get(url)
html_content = response.content

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find the table in the page
table = soup.find('table', class_='table-colored')

# Check if the table was found
if table:
    print('Table found, processing rows...')
else:
    raise ValueError("Table with class 'table-colored' not found.")

# Initialize a list to hold timezone data
timezones_info = list()

# If no tbody, we can just directly search for tr tags within the table
rows = table.find_all('tr')[1:]  # Skip the header row

# Iterate over all rows in the table body
for row in rows:
    # Extract the UTC offset
    utc = row.find('td').strong.text.replace('UTC', '').strip()

    # Extract the timezone
    timezone = row.find_all('td')[1].text.strip()

    # Extract the country name
    country = row.find_all('td')[2].text.strip()

    # Extract cities (if any)
    cities = [city.text.strip() for city in row.find_all('td')[3].find_all('a')]

    # Create a dictionary for each timezone entry
    timezone_data = {
        'timezone': timezone,
        'utc': utc,
        'country': country,
        'cities': cities
    }

    # Append the timezone data to the list
    timezones_info.append(timezone_data)


# Write the result to a JSON file
with open(SCRAPED_TIMEZONES_CITIES_JSON, 'w', encoding='utf-8') as json_file:
    json.dump(timezones_info, json_file, indent=4, ensure_ascii=False)

print(f'Data extracted and saved to {SCRAPED_TIMEZONES_CITIES_JSON}')
