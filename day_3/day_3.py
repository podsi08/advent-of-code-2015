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


def move(i, position):
    if i == ">":
        position[0] += 1
    elif i == "<":
        position[0] -= 1
    elif i == "^":
        position[1] += 1
    else:
        position[1] -= 1
    return position


def part_2(text):
    santa_position = [0, 0]
    robo_santa_position = [0, 0]
    houses_with_present = []

    for i in range(0, len(text)):
        if i % 2 == 0:
            santa_position = move(text[i], santa_position)
        else:
            robo_santa_position = move(text[i], robo_santa_position)

        if santa_position not in houses_with_present:
            houses_with_present.append(santa_position.copy())

        if robo_santa_position not in houses_with_present:
            houses_with_present.append(robo_santa_position.copy())

    return len(houses_with_present)


def main():
    with open("input.txt", "r") as file_input:
        input_text = file_input.read()
        print(part_1(input_text))
        print(part_2(input_text))


if __name__ == '__main__':
    main()