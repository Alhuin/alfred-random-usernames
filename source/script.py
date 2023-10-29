""" This is the script used within the Alfred Workflow, made available for convenient customization. """

import sys
import json
import random
import os


class ConfigurationError(Exception):
    pass


def _validate_env_positive_integer(field_name):
    nb_str = os.getenv(field_name)

    if not nb_str.isdigit() or (nb := int(nb_str)) < 0:
        raise ConfigurationError(f"{field_name} has to be a positive integer.")

    return nb


def _validate_env_txt_file(field_name):
    path = os.getenv(field_name)
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
            "icon": {"path": "./source/icon.png"},
        }
        for username in usernames
    ]


def _get_formatted_error(error):
    return [
        {
            "title": f"ConfigurationError: {error}",
            "valid": False,
            "icon": {"path": "./source/icon.png"},
        }
    ]


def generate_usernames(nb_usernames):
    numbers_range = _validate_env_positive_integer("numbers_range")
    adjectives = _validate_env_txt_file("adjectives_path")
    nouns = _validate_env_txt_file("nouns_path")

    return [
        f"{random.choice(adjectives).capitalize()}{random.choice(nouns).capitalize()}{random.randrange(numbers_range)}"
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
