# alfred-random-usernames
An alfred workflow to generate random usernames to your clipboard!
<img width="715" alt="preview" src="https://github.com/Alhuin/alfred-random-usernames/assets/29608747/e45cea86-49a9-4a2a-b37a-5156357edaae">
<img width="941" alt="Screenshot 2023-10-29 at 19 57 14" src="https://github.com/Alhuin/alfred-random-usernames/assets/29608747/f53a926b-561d-4368-8800-e4440560b8a0">

### Generation
The generated usernames are composed of three parts:
- an adjective
- a noun
- a numbers suffix

### Installation
- Download the workflow from [the latest release](https://github.com/Alhuin/alfred-random-usernames/releases/latest)
- Open it to install with Alfred
- Setup your desired HotKey shortcut

### Configuration
<img width="507" alt="Screenshot 2023-10-30 at 12 25 54" src="https://github.com/Alhuin/alfred-random-usernames/assets/29608747/ab493ccc-6ae2-4e29-ae3e-ae2c65af036e">

5 settings are available:
- `Number of generated usernames`: How many usernames should be generated at once (default is 5)
- `Number suffix max value`: The maximum number of the number suffix (default is 5000)
- `Add a number suffix`: If a number suffix should be added to the usernames (default is True)
- `Custom adjectives dictionary`: Provide your own adjectives dictionnary (default is [src/data/adjectives.txt](src/data/adjectives.txt))
- `Custom nouns dictionary`: Provide your own nouns dictionnary (default is [src/data/nouns.txt](src/data/nouns.txt))
- `Use wonderwords`: external package for random words generation
- `Capitalize adjectives`: If the adjective part of the usernames should be capitalized (default is True)
- `Capitalize nouns`: If the noun part of the usernames should be capitalized (default is True)

### Usage
- Alfred HotKey > `usergen` > select a username > the username is copied
- Workflow HotKey > a random username is copied


### Requirements
- Alfred ^5
- python ^3.9

### Credits
- Generation logic: https://github.com/williexu/random_username
- wonderwords package: https://pypi.org/project/wonderwords/
- Icon: https://www.flaticon.com/free-icon/ninja_1071164
