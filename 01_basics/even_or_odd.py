"""Exercise 3: Even or Odd
Reads an integer from the user and determines if it is even or odd.
"""


def main():
    try:
        number = int(input("Enter an integer: "))
        if number % 2 == 0:
            print(f"{number} is even.")
        else:
            print(f"{number} is odd.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")


if __name__ == "__main__":
    main()
