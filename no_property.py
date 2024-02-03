from collections.abc import Iterator

class Dog:
    def __init__(self, name, breed):
        self.breed = breed
        self.name = name

    def __repr__(self) -> str:
        return f"{self.name} is a {self.breed}"
    
    def __eq__(self, value: object):
        if isinstance(value, Dog):
            return (self.name, self.breed) == (value.name, value.breed)
        return False
    
def main():
    dog1 = Dog("Pomsky", "Buddy")
    dog2 = Dog("Pomsky", "Buddy")
    print(dog1 == dog2)

if __name__ == "__main__":
    main()