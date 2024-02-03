def len_list(list):
    count = 0
    for item in list:
        list[count] = len(str(item))
        count += 1

def main():
    list = [12,456,9000]
    len_list(list)
    print(list)

if __name__ == "__main__":
    main()