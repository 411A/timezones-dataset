import json
from CONSTANTS import (
    FINAL_TIMEZONES_JSON,
    FINAL_UNIQUE_TIMEZONES_JSON
)

# Load the FINAL.json data
with open(FINAL_TIMEZONES_JSON, 'r', encoding='utf-8') as final_file:
    final_data = json.load(final_file)

# Define the filter cities for countries
filter_countries_timezones = {
    'United States': 'New York City',   # Recognizable time zone
    'Russia': 'Moscow',            # Capital
    'Canada': 'Toronto',           # Recognizable time zone
    'Brazil': 'Brasília',          # Capital
    'Mexico': 'Mexico City',       # Capital
    'Argentina': 'Buenos Aires',   # Capital
    'Australia': 'Sydney',         # Recognizable time zone
    'Antarctica': 'McMurdo Station', # Major location
    'Kazakhstan': 'Astana',        # Capital
    'Greenland': 'Nuuk',           # Capital
    'Indonesia': 'Jakarta',        # Capital
    'French Polynesia': 'Papeete', # Capital
    'Chile': 'Santiago',           # Capital
    'Portugal': 'Lisbon',          # Capital
    'Spain': 'Madrid',             # Capital
    'Mongolia': 'Ulaanbaatar',     # Capital
    'Micronesia': 'Palikir',       # Capital
    'Kiribati': 'Tarawa',          # Capital
    'United States Minor Outlying Islands': 'Midway Atoll', # Major location
    'Ecuador': 'Quito',            # Capital
    'Democratic Republic of the Congo': 'Kinshasa', # Capital
    'Cyprus': 'Nicosia',           # Capital
    'Palestinian Territory': 'Ramallah', # Major city
    'Ukraine': 'Kyiv',             # Capital
    'Uzbekistan': 'Tashkent',      # Capital
    'China': 'Beijing',            # Capital
    'Malaysia': 'Kuala Lumpur',    # Capital
    'Papua New Guinea': 'Port Moresby', # Capital
    'New Zealand': 'Wellington',   # Capital
    'Marshall Islands': 'Majuro'   # Capital
}

# Dictionary to hold unique final data for each country
unique_final_data = list()

# Iterate through each UTC group in FINAL.json
for group in final_data:
    utc_offset = group['utc']
    filtered_timezones = list()
    
    # Check each timezone in the group
    for tz in group['timezones']:
        country_name = tz['country_name']
        
        # Check if the country is in the filter list and if the timezone contains the city we are looking for
        if country_name in filter_countries_timezones:
            # Get the city to match for this country
            target_city = filter_countries_timezones[country_name]
            
            # Check if the target city is in this timezone's cities list
            if target_city in tz['country_cities']:
                # Reorder the cities list: target city first, then other cities
                remaining_cities = [city for city in tz['country_cities'] if city != target_city]
                reordered_cities = [target_city] + remaining_cities
                
                # Create a copy of the timezone and update the country_cities field
                filtered_timezone = tz.copy()
                filtered_timezone['country_cities'] = reordered_cities
                filtered_timezones.append(filtered_timezone)
        else:
            # If the country is not in the filter list, include it as is
            filtered_timezones.append(tz)

    if filtered_timezones:
        # If there are valid filtered timezones, append them to the unique final data
        unique_final_data.append({
            'utc': utc_offset,
            'timezones': filtered_timezones
        })

# Save the unique final data to FINAL_UNIQUE_TIMEZONES_JSON
with open(FINAL_UNIQUE_TIMEZONES_JSON, 'w', encoding='utf-8') as unique_file:
    json.dump(unique_final_data, unique_file, ensure_ascii=False, indent=4)

print(f'{FINAL_UNIQUE_TIMEZONES_JSON} generated successfully!')
