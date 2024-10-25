### 🌐 Mutual Timezones Dataset: Countries, Country Codes, Cities and Flags

#### 💌 Thanks to:
* [OpenAI's ChatGPT](https://chat.openai.com): For expediting the process.
* [devhammed](https://gist.github.com/devhammed/78cfbee0c36dfdaa4fce7e79c0d39208): For the `devhammed_countries-flags-codes.json` file.
* [dmfilipenko](https://github.com/dmfilipenko/timezones.json/blob/master/timezones.json): For the `dmfilipenko_timezones.json` file.
* [zeitverschiebung.net](https://zeitverschiebung.net/en/all-time-zones.html): For the timezone data with cities (resulting in `01_scraped-timezones-cities.json`).
* [flagpedia.net](https://flagpedia.net/emoji): For the emoji flags (resulting in `02_scraped-flags.json`).

#### 🔰 Project Steps:

💡 The file names indicate the process themselves.

<details>
  <summary>👣 Steps</summary>

  <p><strong>01</strong>: Scraped timezones and cities.</p>

  <p><strong>02</strong>: Scraped emoji flags.</p>

  <p><strong>03</strong>: Identified countries with multiple timezones.</p>

  <p><strong>04</strong>: First, I consulted ChatGPT and provided the content of <code>03_counted-countries.json</code> to ask for a Python dictionary with capital or widely accepted timezones for countries with multiple timezones. Afterward, I manually researched and verified the results and adapted the city names (values) to match the city names in the JSON from step <em>01</em>.</p>

  <p><strong>05</strong>: Created a JSON file (includes multiple timezones for each country).</p>

  <p><strong>06</strong>: Used the Python dictionary from step <strong>04</strong> to create a JSON file with unique timezones for each country!</p>

</details>

#### 💻 Used by:
This work is done as part of my personal project, [UtAZBot](https://t.me/UtAZBot), an inline utility Telegram bot built with Rust, to display local times for all countries in sorted order.
<img src="https://github.com/user-attachments/assets/e659051b-ec1d-4f38-a0e8-4f9bf77e560f" width="382" height="577">
