import os
import random


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


def generate_usernames(nb_usernames):
    adjectives = _validate_env_txt_file("adjectives_path")
    capitalize_adjectives = os.getenv("capitalize_adjectives") == "1"
    nouns = _validate_env_txt_file("nouns_path")
    capitalize_nouns = os.getenv("capitalize_nouns") == "1"

    if number_suffix := (os.getenv("number_suffix") == "1"):
        number_suffix_range = _validate_env_positive_integer("number_suffix_range")

    return [
        (
            f"{random.choice(adjectives).capitalize() if capitalize_adjectives else random.choice(adjectives)}"
            f"{random.choice(nouns).capitalize() if capitalize_nouns else random.choice(nouns)}"
            f"{random.randrange(number_suffix_range) if number_suffix else ''}"
        )
        for _ in range(nb_usernames)
    ]
