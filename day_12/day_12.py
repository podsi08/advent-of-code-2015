def part_1(text):
    numbers_m = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "-"]
    total = 0
    to_add = ""
    for i in range(len(text) - 1):
        if text[i] in numbers_m:
            to_add += text[i]
            if text[i + 1] not in numbers_m:
                total += int(to_add)
                to_add = ""
    return total


def part_2(text):
    numbers_m = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "-"]
    total = 0
    to_add = ""
    sum_in_object = 0
    open_object = False
    red_object = False
    for i in range(len(text) - 1):
        if not open_object:
            if text[i] in numbers_m:
                to_add += text[i]
                if text[i + 1] not in numbers_m:
                    total += int(to_add)
                    to_add = ""
            elif text[i] == "{":
                open_object = True
        else:
            if text[i:i+3] == "red":
                red_object = True
            if text[i] == "}":
                open_object = False
                red_object = False
                if not red_object:
                    total += sum_in_object
                    sum_in_object = 0
            if not red_object and text[i] in numbers_m:
                to_add += text[i]
                if text[i + 1] not in numbers_m:
                    sum_in_object += int(to_add)
                    to_add = ""
    return total

# uwzględnić obiekty w obiektach
def main():
    with open("input.txt", "r") as file_input:
        text = file_input.read()
        print(part_1(text))
        print(part_2(text))


if __name__ == '__main__':
    main()
