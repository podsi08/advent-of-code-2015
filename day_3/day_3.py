def part_1(text):
    position = [0, 0]
    houses_with_present = []

    for i in text:
        if i == ">":
            position[0] += 1
        elif i == "<":
            position[0] -= 1
        elif i == "^":
            position[1] += 1
        else:
            position[1] -= 1

        if position not in houses_with_present:
            houses_with_present.append(position.copy())

    return len(houses_with_present)


def main():
    with open("input.txt", "r") as file_input:
        input_text = file_input.read()
        print(part_1(input_text))


if __name__ == '__main__':
    main()