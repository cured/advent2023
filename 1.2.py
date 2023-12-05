import requests
replacement_3 = {"one": 1, "two": 2, "six": 6}
replacement_4 = {"four": 4, "five": 5, "nine": 9}
replacement_5 = {"three": 3, "seven": 7, "eight": 8}


def get_digits_from_line(line: str):
    i = 0
    list_with_digits = []
    while i < len(line):
        three = line[i: i + 3]
        if three in replacement_3:
            list_with_digits.append(replacement_3[three])
            i += 1
            continue
        four = line[i: i + 4]
        if four in replacement_4:
            list_with_digits.append(replacement_4[four])
            i += 1
            continue
        five = line[i: i + 5]
        if five in replacement_5:
            list_with_digits.append(replacement_5[five])
            i += 1
            continue

        if line[i].isdigit():
            list_with_digits.append(int(line[i]))

        i += 1

    res = int(list_with_digits[0]) * 10 + int(list_with_digits[-1])
    return res


def main():
    url = "https://pastebin.com/raw/9Jwsmgrm"
    response = requests.get(url)
    s = 0
    for line in response.iter_lines():
        if not line:
            continue
        s += get_digits_from_line(line.decode('utf-8'))

    print(s)


if __name__ == "__main__":
    main()
