### 🌐 Mutual Timezones Dataset: Countries, Country Codes, Cities and Flags

#### 💌 Thanks to:
* [OpenAI's ChatGPT](https://chat.openai.com): For expediting the process.
* [devhammed](https://gist.github.com/devhammed/78cfbee0c36dfdaa4fce7e79c0d39208): For the `devhammed_countries-flags-codes.json` file.
* [dmfilipenko](https://github.com/dmfilipenko/timezones.json/blob/master/timezones.json): For the `dmfilipenko_timezones.json` file.
* [zeitverschiebung.net](https://zeitverschiebung.net/en/all-time-zones.html): For the timezone data with cities (resulting in `01_scraped-timezones-cities.json`).
* [flagpedia.net](https://flagpedia.net/emoji): For the emoji flags (resulting in `02_scraped-flags.json`).

#### 🔰 Project Steps:

💡 The file names indicate the process themselves.

**01**: Scraped timezones and cities.

**02**: Scraped emoji flags.

**03**: Identified countries with multiple timezones.

**04**: First, I consulted ChatGPT and provided the content of `03_counted-countries.json` to ask for a Python dictionary with capital or widely accepted timezones for countries with multiple timezones. Afterward, I manually researched and verified the results and adapted the city names (values) to match the city names in the JSON from step *01*.

**05**: Created a JSON file (includes multiple timezones for each country).

**06**: Used the Python dictionary from step *04* to create a JSON file with unique timezones for each country!
