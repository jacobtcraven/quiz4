import argparse

def cart() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(help = "Enter the store name", dest = "store", type = str)
    parser.add_argument(help = "Enter the number of items in the cart", dest = "num_items", type = int)
    parser.add_argument(help = "Enter the total cost of the items", dest = "total_cost", type = float)

    args = parser.parse_args()

    store = args.store
    num_items = args.num_items
    total_cost = args.total_cost

    print(f"At {store} you have {num_items} items in your cart and the total cost is {total_cost}")

if __name__ == "__main__":
    cart()