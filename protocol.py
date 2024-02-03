from typing import Protocol

class PerManager(Protocol):
    def add(self, item) -> None:
        pass
    
    def clear(self) -> None:
        pass

class backpack:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def clear(self):
        self.items.clear()

class cart:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def clear(self):
        self.items.clear()