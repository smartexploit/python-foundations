""" Multiplication Table
Displays a 10x10 multiplication table with top and side row headers.
"""


def main():
    # Print the top header row (corner space followed by 1 to 10)
    print("    ", end="")
    for col in range(1, 11):
        print(f"{col:>4}", end="")
    print()  # Move to the next line

    # Print each row of the table
    for row in range(1, 11):
        # Print the side header label
        print(f"{row:>4}", end="")

        # Print the products for this row
        for col in range(1, 11):
            product = row * col
            print(f"{product:>4}", end="")

        print()  # Move to the next line after finishing a row


if __name__ == "__main__":
    main()
