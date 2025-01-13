# DefaultMissions
This repo contains the default missions used by Reentry. This includes all the free play missions, the academy lessons, scenarios, campaigns, and the historic missions.

# Unused Missions
The following missions are not in use and should not be transalted. They are there for some users who are using special builds.

Mercury:
- campaign0.json
- campaign1.json
- historicMA6.json
- historicMR3.json
- historicMR4.json

# Languages
Each mission can be translated into any language using a language code as part of their file name.

The following list shows the languages we currently want to support. More will be added as the core of the game gets translated. If you have suggestions please reach out.
|        Language        | code  |
|------------------------|-------|
| Spanish                | es-es |
| Russian                | ru-ru |
| French                 | fr-fr |
| German                 | de-de |
| Chinese (Simplified)   | zh-cn |

## How to contribute
To contribute, you will need to get the mission files stored on your harddrive, pick a language to translate to for a given file that is missing in the status above, use a text editor such as Visual Studio Code, then commit and push the change as a pull request. We will then test and verify, and potentially merge the change into the game.

### 1. Setup
The first step you need to do is to clone or download this repo to your local environment.
Do this by using the clone/download zip button on this repo (Code->Clone/Download Zip)

When you have the repo cloned, all of the mission files can be found in various directories. 

### 2. Structure
Each mission as its english file as the main file, for example mission1.json or lesson1.json. The english file does not contain a language code in its file name.

For the game to would support another language such as de-de (German (Germany)), the english file would need to be translated to German, and saved as:
mission1.**de-de**.json

### 3. Translate
Make a copy of the file or modify an existing if you wish to improve. Let's say you wish to translate mission1.json (english file). Make a copy if mission1.json and rename the file to contain the language code, for example:
mission1.**de-de**.json

Open the file in a text editor such as Visual Studio Code and translate the in-game commands (json format). Do not modify the mission ID or the GUID as these are used to look up mission completion and store progress.

### 4. Contributing your changes
The last step is to submit your changes to us. This is done through a pull request.


## Campaigns
The language structure is similar to campaigns. A campaign is made out of a *.desc file. This is the main file. To translate this, make a copy of it and add in the language code, for example descriptor.**de-de**.desc. Do not modify the Title of the campaign as this is the main ID, but transalte the DisplayTitle (this is what the game uses when showing the name, thus it needs a translation).

Each mission of the campaign works like a normal mission and can be translated like the other missions (see above)


## Using GitHub
Forking a repo
https://docs.github.com/en/get-started/quickstart/fork-a-repo

Submitting your fork as a pull request to the language repo
https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork

For language-codes, see [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) and [ISO 3166-1](https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes) alpha-2. For example, for English as written in the United States, first lookup the ISO 3166-1 alpha 2 code for the United States (**us**), then the ISO 639-1 language-code for English (**en**). For constructed languages, see [ISO-639-2](https://en.wikipedia.org/wiki/List_of_ISO_639-2_codes). For languages that do not belong to a specific country (ex latin), use the language-code as previously specified without a country-code.
