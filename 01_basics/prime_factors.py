""" Prime Factors
Computes and displays the prime factors of an integer (>= 2).
"""


def main():
    try:
        n = int(input("Enter an integer (2 or greater): "))

        if n < 2:
            print("Error: Please enter an integer greater than or equal to 2.")
            return

        print(f"The prime factors of {n} are:")

        # Step 1: Initialize factor to 2
        factor = 2

        # Step 2: Loop while factor <= n
        while factor <= n:
            # Step 3: Check if n is evenly divisible by factor
            if n % factor == 0:
                print(factor)
                n = n // factor  # Divide n by factor using floor division
            else:
                factor += 1  # Increase factor by 1

    except ValueError:
        print("Invalid input. Please enter a valid integer.")


if __name__ == "__main__":
    main()
