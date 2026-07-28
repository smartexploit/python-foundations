""" Prime Numbers
Determines whether an integer is a prime number.
"""


def is_prime(n: int) -> bool:
    """Checks whether an integer n is a prime number."""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    # Check odd divisors up to sqrt(n)
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2

    return True


def main():
    try:
        number = int(input("Enter an integer: "))
        if is_prime(number):
            print(f"{number} is a prime number.")
        else:
            print(f"{number} is not a prime number.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")


# Ensures main() will not execute if imported as a module
if __name__ == "__main__":
    main()
