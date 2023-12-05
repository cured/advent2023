import requests
from regex import findall


def mul(string: str) -> int:
    pattern = "((\d+) (blue|green|red)[, ;]*)"
    found = findall(pattern, string)
    max_red = max_green = max_blue = 0

    for f in found:
        print(f)
        match f[2]:
            case "red":
                if max_red < int(f[1]):
                    max_red = int(f[1])
            case "green":
                if max_green < int(f[1]):
                    max_green = int(f[1])
            case "blue":
                if max_blue < int(f[1]):
                    max_blue = int(f[1])

    return max_red * max_blue * max_green


def main():
    url = "https://pastebin.com/raw/YPAe68XG"
    response = requests.get(url)
    # "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
    sum_ = 0
    for line in response.iter_lines():
        _, cubes = line.decode("utf-8").split(":")
        sum_ += mul(cubes)

    print(sum_)


if __name__ == "__main__":
    main()
