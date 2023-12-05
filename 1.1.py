import requests


def get_digits_from_line(line: str):
    digit_line = [l for l in line if l.isdigit()]
    return int(digit_line[0]) * 10 + int(digit_line[-1])


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
