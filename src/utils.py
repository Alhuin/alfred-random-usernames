import os
import random
import sys

if use_wonderwords := os.getenv("use_wonderwords") == "1":
    lib_path = os.path.join(os.path.dirname(__file__), "lib")
    sys.path.insert(0, lib_path)
    from wonderwords import RandomWord

    r = RandomWord()


class ConfigurationError(Exception):
    pass


def _get_wonderwords(nb, type):
    words = r.random_words(nb, include_categories=[type])
    return words


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
    capitalize_adjectives = os.getenv("capitalize_adjectives") == "1"
    capitalize_nouns = os.getenv("capitalize_nouns") == "1"

    if use_wonderwords:
        adjectives = _get_wonderwords(nb_usernames, "adjectives")
        nouns = _get_wonderwords(nb_usernames, "nouns")
    else:
        adjectives = random.choices(
            _validate_env_txt_file("adjectives_path"), k=nb_usernames
        )
        nouns = random.choices(_validate_env_txt_file("nouns_path"), k=nb_usernames)

    if number_suffix := (os.getenv("number_suffix") == "1"):
        number_suffix_range = _validate_env_positive_integer("number_suffix_range")

    return [
        (
            f"{adjectives[i].capitalize() if capitalize_adjectives else adjectives[i]}"
            f"{nouns[i].capitalize() if capitalize_nouns else nouns[i]}"
            f"{random.randrange(number_suffix_range) if number_suffix else ''}"
        )
        for i in range(nb_usernames)
    ]
