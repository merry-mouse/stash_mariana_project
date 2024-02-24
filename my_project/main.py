import random
import string


def generate_random_string(length=10) -> str:
    random_string = ""
    characters = string.ascii_letters + string.digits
    for i in range(length):
        random_string += random.choice(characters)
    return random_string


if __name__ == "__main__":
    print(generate_random_string())
