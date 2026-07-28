""" Vowel or Consonant
Determines whether an entered letter is a vowel, consonant, or sometimes both (y).
"""


def main():
    letter = input("Enter a letter of the alphabet: ").strip().lower()

    if len(letter) != 1 or not letter.isalpha():
        print("Invalid input. Please enter a single letter.")
        return

    vowels = ("a", "e", "i", "o", "u")

    if letter in vowels:
        print(f"'{letter}' is a vowel.")
    elif letter == "y":
        print("Sometimes 'y' is a vowel, and sometimes 'y' is a consonant.")
    else:
        print(f"'{letter}' is a consonant.")


if __name__ == "__main__":
    main()
