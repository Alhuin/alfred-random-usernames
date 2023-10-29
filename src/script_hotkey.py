import sys
from utils import generate_usernames, ConfigurationError

if __name__ == "__main__":
    try:
        result = generate_usernames(1)[0]
    except ConfigurationError as e:
        result = f"ConfigurationError: {e}"

    sys.stdout.write(result)
