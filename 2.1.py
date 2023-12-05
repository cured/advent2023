import requests
from regex import findall


red = 12
green = 13
blue = 14


def check(string: str) -> bool:
    pattern = "((\d+) (blue|green|red)[, ;]*)"
    found = findall(pattern, string)
    conditions = []
    for f in found:
        print(f)
        match f[2]:
            case "red":
                conditions.append(int(f[1]) <= red)
            case "green":
                conditions.append(int(f[1]) <= green)
            case "blue":
                conditions.append(int(f[1]) <= blue)

    return all(conditions)


def main():
    url = "https://pastebin.com/raw/YPAe68XG"
    response = requests.get(url)
    # "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
    sum_ = 0
    for line in response.iter_lines():
        game, cubes = line.decode("utf-8").split(":")
        game_id = int(game.split(" ")[1])
        if check(cubes):
            sum_ += game_id

    print(sum_)


if __name__ == "__main__":
    main()
