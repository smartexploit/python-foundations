""" Random Password Generator
Generates a password with random length (7 to 10) using ASCII characters 33-126.
"""

import random


def generate_password() -> str:
    """Generates and returns a random password."""
    password_length = random.randint(7, 10)
    password_chars = [chr(random.randint(33, 126)) for _ in range(password_length)]
    return "".join(password_chars)


def main():
    password = generate_password()
    print(f"Randomly generated password: {password}")


if __name__ == "__main__":
    main()
