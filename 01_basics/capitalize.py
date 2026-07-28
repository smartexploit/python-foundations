""" Auto Capitalization
Capitalizes sentences and standalone 'i's in a given string.
"""


def auto_capitalize(text: str) -> str:
    chars = list(text)
    capitalize_next = True

    for idx, char in enumerate(chars):
        # Rules 1 & 2: Capitalize first non-space character or first non-space after punctuation
        if capitalize_next and char != " ":
            chars[idx] = char.upper()
            capitalize_next = False

        # Reset capitalization flag after sentence-ending punctuation
        if char in [".", "!", "?"]:
            capitalize_next = True

        # Rule 3: Capitalize 'i' if preceded by a space and followed by space, punctuation, or apostrophe
        if chars[idx] == "i":
            prev_is_space = (idx == 0) or (chars[idx - 1] == " ")
            next_is_valid = (idx == len(chars) - 1) or (
                chars[idx + 1] in [" ", ".", "!", "?", "'", "’"]
            )

            if prev_is_space and next_is_valid:
                chars[idx] = "I"

    return "".join(chars)


def main():
    user_input = input("Enter a string: ")
    capitalized_text = auto_capitalize(user_input)
    print("\nCapitalized string:")
    print(capitalized_text)


if __name__ == "__main__":
    main()
