from hashlib import md5

def main():
    with open("input.txt", "r") as file_input:
        pass

    print(md5("Ola".encode()).digest())


if __name__ == '__main__':
    main()