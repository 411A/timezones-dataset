from pathlib import Path

# Paths for JSON files inside the Data folder
data_dir = Path("Data").resolve()
# Paths for final JSON files in the parent directory
parent_dir = Path().cwd().resolve()

COUNTRIES_FLAGS_CODES_JSON = data_dir / 'devhammed_countries-flags-codes.json'
TIMEZONES_JSON = data_dir / 'dmfilipenko_timezones.json'
SCRAPED_TIMEZONES_CITIES_JSON = data_dir / '01_scraped-timezones-cities.json'
SCRAPED_FLAGS_JSON = data_dir / '02_scraped-flags.json'
COUNTED_COUNTRIES_JSON = data_dir / '03_counted-countries.json'
FINAL_TIMEZONES_JSON = parent_dir / '05_generated-timezones.json'
FINAL_UNIQUE_TIMEZONES_JSON = parent_dir / '06_generated-unique-timezones.json'
