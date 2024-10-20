'''
Scrapes country flag emojis.
'''

import requests
from bs4 import BeautifulSoup
import json
from CONSTANTS import SCRAPED_FLAGS_JSON

# URL of the page to scrape
url = 'https://flagpedia.net/emoji'

# Send a GET request to the webpage
response = requests.get(url)
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find the table with class 'color'
    table = soup.find('table', class_='color')

    # Initialize a dictionary to store country-emoji pairs
    country_to_emoji = dict()

    # Loop through all the rows in the table body
    for row in table.tbody.find_all('tr'):
        # Extract the emoji (contained in the first <a> tag inside the first <td>)
        emoji = row.find('a', class_='emoji').text.strip()

        # Extract the country name (contained in the second <a> tag)
        country = row.find('td', class_='td-country').a.text.strip()

        # Add the country and its emoji to the dictionary
        country_to_emoji[country] = emoji

    # Write the dictionary to a JSON file
    with open(SCRAPED_FLAGS_JSON, 'w', encoding='utf-8') as f:
        json.dump(country_to_emoji, f, ensure_ascii=False, indent=4)

    print(f'JSON file ({SCRAPED_FLAGS_JSON}) generated successfully!')
else:
    print(f'Failed to retrieve the webpage. Status code: {response.status_code}')
