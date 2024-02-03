from abc import ABC, abstractmethod

class PerManager(ABC):

    @abstractmethod
    def add(self, item):
        pass
    
    @abstractmethod
    def clear(self):
        pass

class backpack(PerManager):
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def clear(self):
        self.items.clear()

class cart(PerManager):
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def clear(self):
        self.items.clear()