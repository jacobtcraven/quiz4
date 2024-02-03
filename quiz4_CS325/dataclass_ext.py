from dataclass import Backpack

def unpack_backpack(backpack):
    return f"{backpack.owner} has a {backpack.computer} and {backpack.number_books} books."

def main():
    my_backpack = Backpack('Jacob', 'MacBook', 3)
    print(unpack_backpack(my_backpack))

if __name__ == "__main__": 
    main()