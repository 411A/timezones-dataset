import json
from CONSTANTS import (
    SCRAPED_TIMEZONES_CITIES_JSON,
    SCRAPED_FLAGS_JSON,
    COUNTRIES_FLAGS_CODES_JSON,
    TIMEZONES_JSON,
    FINAL_TIMEZONES_JSON
)

# Load data from the input files
with open(SCRAPED_TIMEZONES_CITIES_JSON, 'r', encoding='utf-8') as tz_file:
    timezones_data = json.load(tz_file)

with open(SCRAPED_FLAGS_JSON, 'r', encoding='utf-8') as country_emoji_file:
    country_to_emoji = json.load(country_emoji_file)

with open(COUNTRIES_FLAGS_CODES_JSON, 'r', encoding='utf-8') as country_flag_file:
    countries_with_flag_code = json.load(country_flag_file)

with open(TIMEZONES_JSON, 'r', encoding='utf-8') as tz_info_file:
    timezones_info = json.load(tz_info_file)

# Create a lookup dictionary for abbr, dial, and flag for quick reference
country_flag_lookup = {
    country['name']: {
        'abbr': country['code'],
        'dial': country['dial_code'],
        'flag': country['flag']
    }
    for country in countries_with_flag_code
}

# Create a lookup for the TIMEZONES_JSON data based on the 'utc' values
tz_info_lookup = dict()
for tz_info in timezones_info:
    for utc_value in tz_info['utc']:
        tz_info_lookup[utc_value] = {
            'timezone_abbr': tz_info['abbr'],
            'timezone_text': tz_info['value'],
            'timezone_description': tz_info['text'],
            'dst': tz_info['isdst']
        }

final_output = dict()

# Iterate over the timezones and build the final structure
for tz in timezones_data:
    # Timezone details
    timezone_name = tz['timezone']
    utc_offset = tz['utc']
    country_name = tz['country']

    # Fetch the flag either from 02_country-to-emoji or countries-with-flag-code
    flag = country_to_emoji.get(country_name, country_flag_lookup.get(country_name, {}).get('flag'))

    # Fetch abbreviation and dial from countries-with-flag-code
    abbr = country_flag_lookup.get(country_name, {}).get('abbr', '')
    dial = country_flag_lookup.get(country_name, {}).get('dial', '')

    # Match the timezone with TIMEZONES_JSON data by 'utc' value
    timezone_info = tz_info_lookup.get(timezone_name, {})

    # Create the country data enriched with timezone details
    country_info = {
        'timezone_name': timezone_name,
        'timezone_abbr': timezone_info.get('timezone_abbr', ''),
        'timezone_text': timezone_info.get('timezone_text', ''),
        'timezone_description': timezone_info.get('timezone_description', ''),
        'dst': timezone_info.get('dst', False),
        'country_name': country_name,
        'country_abbr': abbr,
        'country_dial': dial,
        'country_flag': flag,
        'country_cities': tz.get('cities', [])
    }

    # Check if the utc offset already exists in the final output
    if utc_offset not in final_output:
        final_output[utc_offset] = {'utc': utc_offset, 'timezones': []}

    # Add the timezone with country info under the correct UTC group
    final_output[utc_offset]['timezones'].append(country_info)

# Convert the final_output dict to a list of values (to match the desired output format)
final_output_list = list(final_output.values())

# Save the final data to FINAL.json
with open(FINAL_TIMEZONES_JSON, 'w', encoding='utf-8') as final_file:
    json.dump(final_output_list, final_file, ensure_ascii=False, indent=4)

print(f'{FINAL_TIMEZONES_JSON} generated successfully!')
