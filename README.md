# alfred-random-usernames
An alfred workflow handling random usernames generation: Select between generated usernames and add the chosen one to the clipboard!

<img width="718" alt="Screenshot 2023-10-29 at 16 35 08" src="https://github.com/Alhuin/alfred-random-usernames/assets/29608747/2c7996b2-3bd8-4921-bcce-36c4ab57c329">
<img width="988" alt="Screenshot 2023-10-29 at 17 38 32" src="https://github.com/Alhuin/alfred-random-usernames/assets/29608747/a641ec3c-bf18-4538-82ac-5ed68ca25775">

### Generation
The generated usernames are composed of three parts:
- an adjective
- a noun
- a numbers suffix

### Configuration
<img width="506" alt="Screenshot 2023-10-29 at 16 58 03" src="https://github.com/Alhuin/alfred-random-usernames/assets/29608747/0366f38e-a293-4e18-8a26-92b782bb72b1">

5 settings are available:
- `Number of generated usernames`: How many usernames should be generated at once (default is 5)
- `Numbers suffix max value`: The maximum number of the numbers suffix (default is 5000)
- `Add a numbers suffix`: If a numbers suffix should be added to the usernames (default is True)
- `Custom adjectives dictionnary`: Provide your own adjectives dictionnary (optional .txt file, example: [data/adjectives](data/adjectives.txt))
- `Capitalize adjectives`: If the adjective part of the usernames should be capitalized (default is True)
- `The nouns file you want to pick from`: Provide your own nouns dictionnary (optional .txt file, example: [data/nouns.txt](data/nouns.txt))
- `Capitalize nouns`: If the noun part of the usernames should be capitalized (default is True)

### Usage
- Alfred HotKey > `usergen` > select a username > the username is copied
- HotKey ⌘⇧U (Customizable in the WorkfLow) > a random username is copied


### Requirements
- Alfred ^5
- python ^3.9

### Credits
Generation logic: https://github.com/williexu/random_username
