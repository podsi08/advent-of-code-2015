def part_1(word):
    vovels = ['a', 'e', 'i', 'o', 'u']
    count_vovels = 0
    double_letters = False
    bad_string = False

    for i in range(0, len(word)):
        if word[i] in vovels:
            count_vovels += 1

        if i <= (len(word) - 2):
            if word[i] == word[i + 1]:
                double_letters = True

        if word.count('ab') >= 1 or word.count('cd') >= 1 or word.count('pq') >= 1 or word.count('xy') >= 1:
            bad_string = True

    if count_vovels >= 3 and double_letters and not bad_string:
        return True


def part_2(word):
    pair_of_letters = False
    history_of_pairs = []
    repeat_letters = False

    for i in range(0, len(word)):
        if 1 <= i <= (len(word) - 2) and word[i] != word[i - 1]:
            if (word[i] + word[i + 1]) in history_of_pairs:
                pair_of_letters = True
            history_of_pairs.append(word[i] + word[i + 1])

        if i <= (len(word) - 3):
            if word[i] == word[i + 2]:
                repeat_letters = True

    if pair_of_letters and repeat_letters:
        return True


def main():
    with open("input.txt", "r") as file_input:
        nice_strings = 0
        for line in file_input:
            if part_1(line):
                nice_strings += 1
        #print(nice_strings)

    with open("input.txt", "r") as file_input:
        nice_strings_2 = 0
        for line in file_input:
            if part_2(line):
                nice_strings_2 += 1
        print(nice_strings_2)


if __name__ == '__main__':
    main()