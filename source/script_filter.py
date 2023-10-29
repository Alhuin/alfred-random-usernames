"""
    This is the script used within the Alfred Workflow for the script_filter part,
    made available for convenient customization.
"""

import sys
import json
import random
import os

default_dicts = {
    "adjectives": [
        "abject",
        "aboard",
        "adoring",
        "affected",
        "alert",
        "aloof",
        "amazed",
        "amused",
        "annoyed",
        "anxious",
        "ardent",
        "artistic",
        "ashamed",
        "awed",
        "betrayed",
        "blissful",
        "boastful",
        "bored",
        "brainy",
        "bubbly",
        "cautious",
        "cheerful",
        "chic",
        "cocky",
        "content",
        "cruel",
        "crummy",
        "crushed",
        "cultured",
        "curious",
        "cynical",
        "dear",
        "debonair",
        "decimal",
        "dejected",
        "dopey",
        "dreadful",
        "dreary",
        "eager",
        "ecstatic",
        "empathic",
        "empty",
        "enraged",
        "envious",
        "euphoric",
        "exacting",
        "excited",
        "excluded",
        "fervent",
        "finicky",
        "fond",
        "forsaken",
        "giddy",
        "gleeful",
        "gloomy",
        "goofy",
        "grizzled",
        "grudging",
        "grumpy",
        "guilty",
        "guttural",
        "holistic",
        "humorous",
        "hushed",
        "imported",
        "innocent",
        "insecure",
        "jealous",
        "joyful",
        "jubilant",
        "jumpy",
        "kind",
        "lazy",
        "lovesick",
        "lying",
        "mad",
        "mellow",
        "merciful",
        "mere",
        "mild",
        "morbid",
        "murky",
        "needful",
        "needy",
        "obsessed",
        "offended",
        "outlying",
        "pacified",
        "panicky",
        "peaceful",
        "pesky",
        "pitiful",
        "pleased",
        "plucky",
        "prideful",
        "puzzled",
        "relieved",
        "resolved",
        "sad",
        "scornful",
        "selfish",
        "shameful",
        "sheepish",
        "shy",
        "similar",
        "sincere",
        "solemn",
        "solid",
        "somber",
        "sore",
        "spirited",
        "stressed",
        "sugary",
        "superior",
        "taut",
        "thrifty",
        "thrilled",
        "troubled",
        "trusting",
        "truthful",
        "unhappy",
        "vengeful",
        "wakeful",
        "weary",
        "winged",
        "worldly",
        "wornout",
        "worried",
        "wrathful",
        "yearning",
        "zesty"
    ],
    "nouns": [
        "abalone",
        "antelope",
        "apples",
        "apricots",
        "baboon",
        "bagels",
        "basmati",
        "bass",
        "bittern",
        "boa",
        "boars",
        "bobolink",
        "buck",
        "burritos",
        "bustard",
        "buzzard",
        "cake",
        "camel",
        "cardinal",
        "caribou",
        "caviar",
        "chamois",
        "cheese",
        "cheetah",
        "chile",
        "chough",
        "chowder",
        "clam",
        "coati",
        "cockatoo",
        "coconut",
        "cod",
        "cordial",
        "cow",
        "crackers",
        "crane",
        "cur",
        "curlew",
        "dingo",
        "dinosaur",
        "dotterel",
        "doughnut",
        "dove",
        "doves",
        "dunbird",
        "eagle",
        "eggs",
        "eland",
        "falcon",
        "ferret",
        "fish",
        "flamingo",
        "garlic",
        "gatorade",
        "gelding",
        "gnu",
        "granola",
        "hare",
        "hawk",
        "heron",
        "hoopoe",
        "hyena",
        "icecream",
        "iguana",
        "jaguar",
        "jerky",
        "kitten",
        "lapwing",
        "lard",
        "lemur",
        "leopard",
        "lion",
        "lizard",
        "llama",
        "locust",
        "lollies",
        "macaw",
        "mackerel",
        "magpie",
        "mallard",
        "mandrill",
        "mare",
        "meerkat",
        "moth",
        "muesli",
        "mussel",
        "oatmeal",
        "ocelot",
        "oil",
        "orange",
        "oryx",
        "otter",
        "owl",
        "paella",
        "pear",
        "pepper",
        "pie",
        "piglet",
        "plover",
        "polenta",
        "ponie",
        "porpoise",
        "poultry",
        "pretzels",
        "pudding",
        "pup",
        "quiche",
        "raisins",
        "rat",
        "relish",
        "rhino",
        "rice",
        "ruffs",
        "salami",
        "salt",
        "sardines",
        "sausage",
        "seafowl",
        "seagull",
        "seahorse",
        "shads",
        "sheep",
        "smelt",
        "snail",
        "snipe",
        "stork",
        "swift",
        "syrup",
        "tacos",
        "teal",
        "termite",
        "thrush",
        "thrushe",
        "tomatoe",
        "tortoise",
        "toucan",
        "truffle",
        "tuna",
        "unicorn",
        "venison",
        "viper",
        "wasp",
        "weaver",
        "whiting",
        "widgeon",
        "wigeon",
        "wildfowl",
        "zebra"
    ]
}


class ConfigurationError(Exception):
    pass


def _validate_env_positive_integer(field_name):
    nb_str = os.getenv(field_name)

    if not nb_str.isdigit() or (nb := int(nb_str)) < 0:
        raise ConfigurationError(f"{field_name} has to be a positive integer.")

    return nb


def _validate_env_txt_file(field_name):
    if not (path := os.getenv(field_name)):
        return default_dicts[field_name]

    _, file_extension = os.path.splitext(path)

    if file_extension != ".txt":
        raise ConfigurationError(f"{field_name} has to be a .txt file.")

    with open(path, "r") as fd:
        if not (content := fd.read().splitlines()):
            raise ConfigurationError(f"{field_name} cannot be an empty file.")

    return content


def _get_formatted_results(usernames):
    return [
        {
            "title": username,
            "arg": username,
            "icon": {"path": "./icon.png"},
        }
        for username in usernames
    ]


def _get_formatted_error(error):
    return [
        {
            "title": f"ConfigurationError: {error}",
            "valid": False,
            "icon": {"path": "./icon.png"},
        }
    ]


def generate_usernames(nb_usernames):
    adjectives = _validate_env_txt_file("adjectives_path")
    capitalize_adjectives = os.getenv("capitalize_adjectives") == "1"
    nouns = _validate_env_txt_file("nouns_path")
    capitalize_nouns = os.getenv("capitalize_nouns") == "1"

    if numbers_suffix := (os.getenv("numbers_suffix") == "1"):
        numbers_suffix_range = _validate_env_positive_integer("numbers_suffix_range")

    return [
        (
            f"{random.choice(adjectives).capitalize() if capitalize_adjectives else random.choice(adjectives)}"
            f"{random.choice(nouns).capitalize() if capitalize_nouns else random.choice(nouns)}"
            f"{random.randrange(numbers_suffix_range) if numbers_suffix else ''}"
        )
        for _ in range(nb_usernames)
    ]


if __name__ == "__main__":
    try:
        number_usernames = _validate_env_positive_integer("number_usernames")
        results = generate_usernames(number_usernames)
        alfred_json = json.dumps({"items": _get_formatted_results(results)}, indent=2)
    except ConfigurationError as e:
        alfred_json = json.dumps({"items": _get_formatted_error(e)}, indent=2)

    sys.stdout.write(alfred_json)
