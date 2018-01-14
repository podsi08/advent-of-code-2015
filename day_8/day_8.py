def part_1(text):
    number_of_characters = len(text)
    number_of_characters_2 = 0
    skip = 0
    for i in range(number_of_characters):
        if skip == 0:
            if text[i] == '\\' and (text[i + 1] == '\\' or text[i + 1] == '"'):
                skip = 1
                number_of_characters_2 += 1
            elif text[i] == '\\' and text[i + 1] == 'x':
                skip = 3
                number_of_characters_2 += 1
            elif text[i] == '"':
                continue
            else:
                number_of_characters_2 += 1
        else:
            skip -= 1
    return number_of_characters - number_of_characters_2


def main():
    with open("input.txt", "r") as file_input:
        result = 0
        for line in file_input:
            result += part_1(line.strip())
        print(result)


if __name__ == '__main__':
    main()