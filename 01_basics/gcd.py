""" Greatest Common Divisor
Finds the GCD of two positive integers using a decrementing loop.
"""


def main():
    try:
        n = int(input("Enter the first positive integer: "))
        m = int(input("Enter the second positive integer: "))

        if n <= 0 or m <= 0:
            print("Please enter positive integers only.")
            return

        # Step 1: Initialize d to the smaller of n and m
        d = min(n, m)

        # Step 2: While d does not evenly divide m OR d does not evenly divide n
        while m % d != 0 or n % d != 0:
            d -= 1

        # Step 3: Report d as the greatest common divisor
        print(f"The greatest common divisor of {n} and {m} is {d}.")

    except ValueError:
        print("Invalid input. Please enter valid integers.")


if __name__ == "__main__":
    main()
