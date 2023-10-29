import sys
import json
from utils import _validate_env_positive_integer, generate_usernames, ConfigurationError


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


if __name__ == "__main__":
    try:
        number_usernames = _validate_env_positive_integer("number_usernames")
        results = generate_usernames(number_usernames)
        alfred_json = json.dumps({"items": _get_formatted_results(results)}, indent=2)
    except ConfigurationError as e:
        alfred_json = json.dumps({"items": _get_formatted_error(e)}, indent=2)

    sys.stdout.write(alfred_json)
