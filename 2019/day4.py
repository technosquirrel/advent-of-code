def main():

    input = [138307, 654504]

    part1 = 0
    part2 = 0
    for i in range(input[0], input[1] + 1):
        if isValid(i):
            part1 += 1
            if isValid2(i):
                part2 += 1

    print(part1)
    print(part2)


def isValid(n):

    password = [x for x in str(n)]

    if int("".join(sorted(password))) != n:
        return False
    
    if len(password) == len(set(password)):
        return False
    else:
        return True
    

def isValid2(n):

    password = str(n)
    d = {}
    for c in password:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    
    for c in d:
        if d[c] == 2:
            return True
    
    return False


if __name__ == "__main__":
    main()