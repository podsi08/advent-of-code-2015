def part1(input_text):
    floor = 0
    for i in input_text:
        if i == "(":
            floor += 1
        else:
            floor -= 1
    return floor


def part2(input_text):
    floor = 0
    position = 0
    while floor >= 0:
        if input_text[position] == "(":
            floor += 1
        else:
            floor -= 1
        position += 1
    return position


def main():
    with open("input.txt", "r") as file_input:
        text = file_input.read()

        print(part1(text))
        print(part2(text))


if __name__ == "__main__":
    main()