def look_and_say(text, n):
    step = 0
    count = 0
    new_text = ""

    while step < n:
        for i in range(0, len(text)):
            if i == (len(text) - 1) or text[i] != text[i + 1]:
                if count > 0:
                    count += 1
                    new_text += str(count) + text[i]
                    count = 0
                else:
                    new_text += "1" + text[i]
            elif text[i] == text[i + 1]:
                count += 1
        text = new_text
        new_text = ""
        step += 1
    return len(text)


def main():
    puzzle_input = "1113222113"
    print(look_and_say(puzzle_input, 40))
    print(look_and_say(puzzle_input, 50))


if __name__ == '__main__':
    main()