from collections.abc import Iterator

class Dog:
    def __init__(self, name, breed):
        self._breed = breed
        self._name = name

    @property 
    def name(self):
        return self._name, self._breed
    
    @name.setter                          
    def name(self, new_name):
        if not isinstance(new_name,str):
            val1,val2 = new_name
        else:
            val1=new_name
            val2="No Input"
        self._breed=val1
        self._name = val2

def main():

    dog = Dog("Pomsky", "Buddy")
    print("The Dog's name is:", dog.name)

    dog.name = "Nala"
    print("New name", dog.name)

if __name__ == "__main__":
    main()