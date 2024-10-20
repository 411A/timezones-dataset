'''
Counts countries that have different timezones (like: America/Los_Angeles, America/Chicago),
then they can be managed manualy to use the timezone of the country's capital.
'''

import json
from collections import Counter
from CONSTANTS import SCRAPED_TIMEZONES_CITIES_JSON, COUNTED_COUNTRIES_JSON

# Load the JSON file
with open(SCRAPED_TIMEZONES_CITIES_JSON, 'r', encoding='utf-8') as file:
    data = json.load(file)

# Extract all country names from the JSON
countries = [entry['country'] for entry in data]

# Count occurrences of each country
country_counts = Counter(countries)

# Filter countries that appear more than once
repeated_countries = {country: count for country, count in country_counts.items() if count > 1}
repeated_countries = dict(sorted(repeated_countries.items(), key=lambda item: item[1], reverse=True))

# Print the results
print('Countries appearing more than once:')
for country, count in repeated_countries.items():
    print(f'{country}: {count}')


# Optionally, save the results to a JSON file
with open(COUNTED_COUNTRIES_JSON, 'w', encoding='utf-8') as out_file:
    json.dump(repeated_countries, out_file, indent=4, ensure_ascii=False)

print(f'\nResults saved to {COUNTED_COUNTRIES_JSON}.')

