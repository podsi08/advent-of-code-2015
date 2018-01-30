import json


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


def sum_array(array):
    sum_a = 0
    for element in array:
        if type(element) is int:
            sum_a += element
        elif type(element) is list:
            sum_a += sum_array(element)
        elif type(element) is dict:
            sum_a += sum_object(element)
    return sum_a


def sum_object(object):
    sum_o = 0
    if "red" not in object.values():
        for value in object:
            if type(object[value]) is int:
                sum_o += object[value]
            elif type(object[value]) is list:
                sum_o += sum_array(object[value])
            elif type(object[value]) is dict:
                sum_o += sum_object(object[value])
    return sum_o


def part_2(lst):
    total = 0
    for i in lst:
        if type(i) is list:
            total += sum_array(i)
        elif type(i) is dict:
            total += sum_object(i)
        elif type(i) is int:
            total += i
    return total


def main():
    with open("input.txt", "r") as file_input:
        text = file_input.read()
        print(part_1(text))
        print(part_2(json.loads(text)))


if __name__ == '__main__':
    main()
