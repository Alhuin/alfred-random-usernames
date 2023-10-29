# alfred-random-usernames
An alfred workflow to generate random usernames to your clipboard!
<img width="715" alt="preview" src="https://github.com/Alhuin/alfred-random-usernames/assets/29608747/e45cea86-49a9-4a2a-b37a-5156357edaae">
<img width="941" alt="Screenshot 2023-10-29 at 19 57 14" src="https://github.com/Alhuin/alfred-random-usernames/assets/29608747/f53a926b-561d-4368-8800-e4440560b8a0">

### Generation
The generated usernames are composed of three parts:
- an adjective
- a noun
- a numbers suffix

### Configuration
<img width="504" alt="Screenshot 2023-10-29 at 19 58 33" src="https://github.com/Alhuin/alfred-random-usernames/assets/29608747/3951b431-18e3-4036-9fc7-f710ad2f5fdd">

5 settings are available:
- `Number of generated usernames`: How many usernames should be generated at once (default is 5)
- `Numbers suffix max value`: The maximum number of the numbers suffix (default is 5000)
- `Add a numbers suffix`: If a numbers suffix should be added to the usernames (default is True)
- `Custom adjectives dictionary`: Provide your own adjectives dictionnary (optional .txt file, example: [data/adjectives](data/adjectives.txt))
- `Capitalize adjectives`: If the adjective part of the usernames should be capitalized (default is True)
- `Custom adjectives dictionary`: Provide your own nouns dictionnary (optional .txt file, example: [data/nouns.txt](data/nouns.txt))
- `Capitalize nouns`: If the noun part of the usernames should be capitalized (default is True)

### Usage
- Alfred HotKey > `usergen` > select a username > the username is copied
- Workflow HotKey > a random username is copied


### Requirements
- Alfred ^5
- python ^3.9

### Credits
- Generation logic: https://github.com/williexu/random_username
- Icon: https://www.flaticon.com/free-icon/ninja_1071164
