"""E-Commerce Catalog Engine
Demonstrates OOP Inheritance, super(), Method Overriding, and Polymorphism.
"""

from typing import List


class Product:
    """Base Product class representing a generic catalog item."""

    def __init__(self, product_id: str, name: str, price: float):
        self.product_id = product_id
        self.name = name
        self.price = price

    def get_total_price(self, quantity: int = 1) -> float:
        """Calculates total cost for a given quantity."""
        return self.price * quantity

    def display_details(self) -> None:
        """Prints formatted details of the product."""
        print(f"[{self.product_id}] {self.name} - Base Price: ${self.price:.2f}")


class PhysicalProduct(Product):
    """Subclass representing physical goods that require shipping."""

    SHIPPING_RATE_PER_KG = 5.00  # $5 shipping per kg

    def __init__(self, product_id: str, name: str, price: float, weight_kg: float):
        # Call superclass constructor to handle shared attributes
        super().__init__(product_id, name, price)
        self.weight_kg = weight_kg

    def get_total_price(self, quantity: int = 1) -> float:
        """Calculates total cost including shipping fee based on weight."""
        base_cost = super().get_total_price(quantity)
        shipping_fee = self.weight_kg * self.SHIPPING_RATE_PER_KG * quantity
        return base_cost + shipping_fee

    def display_details(self) -> None:
        """Overrides base display to include physical weight information."""
        print(
            f"[Physical #{self.product_id}] {self.name} | "
            f"Price: ${self.price:.2f} | Weight: {self.weight_kg}kg"
        )


class DigitalProduct(Product):
    """Subclass representing downloadable items with no physical shipping."""

    PROCESSING_FEE = 0.99  # Flat digital handling fee

    def __init__(self, product_id: str, name: str, price: float, file_size_mb: float):
        # Call superclass constructor to handle shared attributes
        super().__init__(product_id, name, price)
        self.file_size_mb = file_size_mb

    def get_total_price(self, quantity: int = 1) -> float:
        """Calculates total cost including a flat digital processing fee."""
        base_cost = super().get_total_price(quantity)
        return base_cost + self.PROCESSING_FEE

    def display_details(self) -> None:
        """Overrides base display to include file size information."""
        print(
            f"[Digital #{self.product_id}] {self.name} | "
            f"Price: ${self.price:.2f} | File Size: {self.file_size_mb}MB"
        )


def process_order(cart: List[Product]) -> None:
    """Demonstrates Polymorphism: Processes different Product types uniformly."""
    print("\n--- Processing Shopping Cart Order ---")
    grand_total = 0.0

    for item in cart:
        # Polymorphic call: Python automatically calls the correct subclass method
        item.display_details()
        item_total = item.get_total_price(quantity=1)
        grand_total += item_total
        print(f"   -> Final Price (incl. fees): ${item_total:.2f}\n")

    print(f"Total Cart Amount Due: ${grand_total:.2f}")


def main():
    # Instantiate Physical and Digital Products
    laptop = PhysicalProduct("P101", "HP EliteBook Laptop", 750.00, weight_kg=1.8)
    ebook = DigitalProduct("D202", "Python Foundations E-Book", 29.99, file_size_mb=15.4)
    headphones = PhysicalProduct("P103", "Wireless Headphones", 89.50, weight_kg=0.4)

    # Place items into a single polymorphic list
    shopping_cart: List[Product] = [laptop, ebook, headphones]

    # Process cart
    process_order(shopping_cart)


if __name__ == "__main__":
    main()
