from hashlib import md5


def part_1(data):
    result = ""
    add = 1
    while result[:5] != "00000":
        text = data + str(add)
        result = md5(text.encode()).hexdigest()
        add += 1
    return add - 1


def part_2(data):
    result = ""
    add = 1
    while result[:6] != "000000":
        text = data + str(add)
        result = md5(text.encode()).hexdigest()
        add += 1
    return add - 1


def main():
    data = "yzbqklnj"
    print(part_1(data))
    print(part_2(data))


if __name__ == '__main__':
    main()