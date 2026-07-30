""" Contact Book & Directory
Demonstrates Lists, Slicing, Dictionaries, and Mutability.
"""

from typing import Dict, Any

# Type alias for clarity
Contact = Dict[str, str]
Directory = Dict[str, Contact]


def add_contact(directory: Directory, name: str, phone: str, email: str) -> None:
    """Adds a new contact or updates an existing one."""
    directory[name] = {"phone": phone, "email": email}
    print(f"[+] Contact '{name}' saved successfully.")


def search_contacts(directory: Directory, query: str) -> None:
    """Searches contacts using case-insensitive partial matching and slicing."""
    query_lower = query.lower()

    # Find matching names
    matches = [
        name for name in directory if query_lower in name.lower()
    ]

    if not matches:
        print(f"[-] No contacts found matching '{query}'.")
        return

    print(f"\n[ Search Results ({len(matches)} found) ]")
    # Demonstrate slicing: Display at most top 5 matches
    for name in matches[:5]:
        details = directory[name]
        print(f" • {name}: Phone={details['phone']} | Email={details['email']}")


def update_contact_phone(directory: Directory, name: str, new_phone: str) -> bool:
    """Demonstrates dictionary mutability by updating a phone number in place."""
    if name in directory:
        directory[name]["phone"] = new_phone
        print(f"[+] Phone number updated for '{name}'.")
        return True
    print(f"[-] Contact '{name}' not found.")
    return False


def main():
    # Initialize empty directory (Dictionary)
    directory: Directory = {}

    # Seed initial data
    add_contact(directory, "Alice Smith", "555-0101", "alice@gmail.com")
    add_contact(directory, "Alexander Graham", "555-0102", "alex@gmail.com")
    add_contact(directory, "Bob Jones", "555-0103", "bob@gmail.com")

    # Search demonstration
    print("\n--- Searching for 'al' ---")
    search_contacts(directory, "al")

    # Mutability demonstration
    print("\n--- Updating Contact ---")
    update_contact_phone(directory, "Alice Smith", "555-9999")

    # Verify update
    print("\n--- Verifying Updated Record ---")
    search_contacts(directory, "Alice")


if __name__ == "__main__":
    main()
