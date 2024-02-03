from dataclasses import dataclass
from collections.abc import Iterator

@dataclass
class Backpack:
    owner: str
    computer: str
    number_books: int

