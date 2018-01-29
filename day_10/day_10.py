def look_and_say(text):
    step = 0
    count = 0
    new_text = ""
    history = []
    while step <= 40:
        for i in range(0, len(text)):
            if i < (len(text) - 1):
                if text[i] == text[i + 1]:
                    count += 1
                else:
                    if count > 0:
                        count += 1
                        new_text += str(count) + text[i]
                        count = 0
                    else:
                        new_text += "1" + text[i]
            else:

        history.append(new_text)
        step += 1


def main():
    puzzle_input = "1113222113"
    print(look_and_say(puzzle_input))


if __name__ == '__main__':
    main()