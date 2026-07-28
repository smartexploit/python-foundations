""" Password Validator
Checks whether a password meets security standards:
- At least 8 characters long
- At least one uppercase letter
- At least one lowercase letter
- At least one digit
"""


def is_good_password(password: str) -> bool:
    """Returns True if the password meets all security criteria, False otherwise."""
    if len(password) < 8:
        return False

    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)

    return has_upper and has_lower and has_digit


def main():
    user_password = input("Enter a password to evaluate: ")

    if is_good_password(user_password):
        print("That is a good password.")
    else:
        print("That password does not meet the requirements.")


if __name__ == "__main__":
    main()
