# Languages
This document will explain how mission translation works in Reentry.

The language can be selected from SETTINGS. The dropdown will change the perferred language. The default language is english and will be the language that will be used if no translation exists for a particular mission.
A mission translated mission will have the language code as part of its filename if translated. A mission file with no language code is the default english mission.

## Status
This section will contain a table with the status of mission translation. Each mission will have a row with a status code for each language as a column.
### MERCURY
#### Academy
| Mission                                                           | Spanish | Russian | French | German |   |   |
|-------------------------------------------------------------------|---------|---------|--------|--------|---|---|
| LESSON 1 - PRE-LAUNCH</br>mercuryTutorialPreLaunch.json           |    0%     |         |        |        |   |   |
| LESSON 2 - LAUNCH & ASCENT</br>mercuryTutorialLaunchAscent.json   |         |         |        |        |   |   |
| LESSON 3 - CHECKLISTS & ATLAS</br>mercuryTutorialAtlasAscent.json |         |         |        |        |   |   |
| LESSON 4 - ELECTRICITY</br>mercuryTutorialEPS.json                |         |         |        |        |   |   |
| LESSON 5 - ATTITUDE CONTROL</br>mercuryTutorialRCS.json           |         |         |        |        |   |   |
| LESSON 6 - STAYING ALIVE</br>mercuryTutorialECS.json              |         |         |        |        |   |   |
| LESSON 7 - SEQUENCER</br>mercuryTutorialSequencer.json            |         |         |        |        |   |   |
| EXAM - FULL MISSION</br>mercuryTutorialFullMission.json           |         |         |        |        |   |   |
| VIRTUAL REALITY</br>mercuryTutorialVR.json                        |         |         |        |        |   |   |

#### Campaign
| Mission                                                 | Spanish | Russian | French | German |   |   |
|---------------------------------------------------------|---------|---------|--------|--------|---|---|
| Campaign Descriptor file                                |         |         |        |        |   |   |
| Mission 1                                               |         |         |        |        |   |   |
| Mission 2                                               |         |         |        |        |   |   |
| Mission 3                                               |         |         |        |        |   |   |
| Mission 4                                               |         |         |        |        |   |   |
| Mission 5                                               |         |         |        |        |   |   |

## Translating
The in-game tool can be used to translate. The process is similar to the one in https://github.com/ReentryGame/Languages.
To contribute, you will need to get the mission files stored on your harddrive, pick a language to translate to for a given file that is missing in the status above, use the in-game tool to translate (or a text editor), then commit and push the change as a pull request. We will then test and verify, and potentially merge the change into the game.

| Language | code |
|----------|------|
| Spanish  | es   |
| Russian  | ru   |
| French   | fr   |
| German   | de   |
|          |      |

### 1. Setup
The first step you need to do is to clone or download this repo to your local environment. Do this by using the clone/download zip button on this repo (Code->Clone/Download Zip)

When you have the repo cloned, all of the mission files can be found in various directories. These files will be loaded when a player selects a mission. If the mission exists with the lanugage code, it will pick this over the english version. These files can be opened by the Reentry Mission Translation tool (Main Menu->Contribute->Translate).

### 2. Structure
The data is stored in different language files. Each mission has at least one file, and each of the supported modules have their own language file(s), and a common that is shared between all of them.
C:\repos\DefaultMissions\Mercury\mercuryTutorialPreLaunch.json

A translated file will have the language code at the end for the file name. If it would be translated to Norwegian (nb-no) then the path would be:
C:\repos\DefaultMissions\Mercury\mercuryTutorialPreLaunch.**nb-no**.json

### 3. Translate
Copy the absolute path and the file name of the mission you wish to translate (english base file). For example:
C:\repos\DefaultMissions\Mercury\mercuryTutorialPreLaunch.json

Start Reentry, and press CONTRIBUTE on the Main Menu, then launch the TRANSLATE MISSION tools.
Paste the absolute path to the file you wish to translate and press LOAD.

When loaded, you can either start a new translation by inserting the language code (see table above) that you wish to translate to, or load an existing translation by pressing Continue and pasting in the absolute path to the translated mission file such as:
C:\repos\DefaultMissions\Mercury\mercuryTutorialPreLaunch.**nb-no**.json

When done, press SAVE.

### 4. Contributing your changes
The last step is to submit your changes to us. This is done through a pull request.
