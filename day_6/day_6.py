import re


def main():
    with open("input.txt", "r") as file_input:
        pattern = re.compile(
            "^(?P<instruction>((turn on)|(turn off)|toggle)) "
            "(?P<col_1>\d+),"
            "(?P<row_1>\d+) through "
            "(?P<col_2>\d+),"
            "(?P<row_2>\d+)$"
        )

        lights = []
        for i in range(1000):
            lights.append([False] * 1000)

        for line in file_input:
            match = pattern.match(line)
            if match is not None:
                instruction = match.group("instruction")
                col_1 = int(match.group("col_1"))
                row_1 = int(match.group("row_1"))
                col_2 = int(match.group("col_2"))
                row_2 = int(match.group("row_2"))

                for row in range(row_1, row_2 + 1):
                    for col in range(col_1, col_2 + 1):
                        if instruction == "turn on":
                            lights[row][col] = True
                        elif instruction == "turn off":
                            lights[row][col] = False
                        elif instruction == "toggle":
                            lights[row][col] = not lights[row][col]

        lights_on = 0
        for row in range(1000):
            for col in range(1000):
                if lights[row][col]:
                    lights_on += 1
        print(lights_on)

    with open("input.txt", "r") as file_input:
        pattern = re.compile(
            "^(?P<instruction>((turn on)|(turn off)|toggle)) "
            "(?P<col_1>\d+),"
            "(?P<row_1>\d+) through "
            "(?P<col_2>\d+),"
            "(?P<row_2>\d+)$"
        )

        lights = []
        for i in range(1000):
            lights.append([0] * 1000)

        for line in file_input:
            match = pattern.match(line)
            if match is not None:
                instruction = match.group("instruction")
                col_1 = int(match.group("col_1"))
                row_1 = int(match.group("row_1"))
                col_2 = int(match.group("col_2"))
                row_2 = int(match.group("row_2"))

                for row in range(row_1, row_2 + 1):
                    for col in range(col_1, col_2 + 1):
                        if instruction == "turn on":
                            lights[row][col] += 1
                        elif instruction == "turn off":
                            if lights[row][col] >= 1:
                                lights[row][col] -= 1
                        elif instruction == "toggle":
                            lights[row][col] += 2

        total_brightness = 0
        for row in range(1000):
            for col in range(1000):
                total_brightness += lights[row][col]
        print(total_brightness)


if __name__ == '__main__':
    main()