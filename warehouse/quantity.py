"""Parse pick-list quantities."""


def parse_quantity(value: str) -> int:
    """Parse a nonnegative integer quantity, raising ValueError if invalid."""
    quantity = int(value.strip())
    if quantity < 0:
        raise ValueError("Quantity must be nonnegative")
    return quantity
