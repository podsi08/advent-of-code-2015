import re


def part_1(l, w, h):
    list_1 = [l, w, h]
    list_1.sort()
    area = 2 * (l * w + l * h + w * h) + list_1[0] * list_1[1]
    return area


def part_2(l, w, h):
    list_1 = [l, w, h]
    list_1.sort()
    total_length = 2 * (list_1[0] + list_1[1]) + l * w * h
    return total_length

def main():
    with open("input.txt", "r") as file_input:
        pattern = re.compile(
            "^(?P<length>\d+)x"
            "(?P<width>\d+)x"
            "(?P<height>\d+)$"
        )

        paper_area = 0
        ribbon = 0

        for line in file_input:
            match = pattern.match(line)
            if match is not None:
                length = int(match.group("length"))
                width = int(match.group("width"))
                height = int(match.group("height"))

            paper_area += part_1(length, width, height)
            ribbon += part_2(length, width, height)

        print(paper_area)
        print(ribbon)




if __name__ == '__main__':
    main()