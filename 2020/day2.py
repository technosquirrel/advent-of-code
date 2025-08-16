import re

def main():

    passwords = parseInput("input.txt")

    part1 = 0
    part2 = 0
    for password in passwords:
        if isValid(password):
            part1 += 1
        if isValid2(password):
            part2 += 1
    print(part1, part2)


def parseInput(f):
    buffer = []
    with open(f) as file:
        for line in file:
            matches = re.search(r"(\d+)-(\d+) (\w): (\w+)", line)
            buffer.append([int(matches[1]), int(matches[2]), matches[3], matches[4]])
    return buffer


def isValid(password):
    if password[0] <= len([x for x in password[3] if x == password[2]]) <= password[1]:
        return True
    return False


def isValid2(password):
    if (password[3][password[0] - 1] == password[2]) ^ (password[3][password[1] - 1] == password[2]):
        return True
    return False


if __name__ == "__main__":
    main()