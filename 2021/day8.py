def main():

    data = parseInput("input.txt")
    
    part1 = 0

    for line in data:
        for x in line[1]:
            if len(x) in [2, 3, 4, 7]:
                part1 += 1
    
    print(part1)


    part2 = 0
    for line in data:
        nums = unscrambleSignals(line[0])
        buffer = []
        for n in line[1]:
            for num in nums:
                if len(n) == len(num) and all(True if x in num else False for x in n):
                    buffer.append(nums[num])
        x = int("".join(str(x) for x in buffer))
        part2 += x
    print(part2)


def parseInput(f):
    with open(f) as file:
        return [[x.split() for x in line.strip().split(" | ")] for line in file]
    

def unscrambleSignals(data):

    unscrambled = {
        "a" : "",
        "b" : "",
        "c" : "",
        "d" : "",
        "e" : "",
        "f" : "",
        "g" : ""
    }

    data.sort(key=lambda x: len(x))

    nums = {
        0 : 0,
        1 : data[0],
        2 : 0,
        3 : 0,
        4 : data[2],
        5 : 0,
        6 : 0,
        7 : data[1],
        8 : data[9],
        9 : 0,
    }

    unscrambled["a"] = [x for x in nums[7] if x not in nums[1]][0]

    for n in data[6:9]:
        if all(True if x in n else False for x in nums[4]) and unscrambled["a"] in n:
            nums[9] = n
            for x in n:
                if x not in nums[4] and x != unscrambled["a"]:
                    unscrambled["g"] = x
    
    unscrambled["e"] = [x for x in nums[8] if x not in nums[9]][0]

    for n in data[3:6]:
        if all(True if x in n else False for x in nums[1]):
            nums[3] = n
            for x in n:
                if x not in data[1] and x!= unscrambled["a"] and x!= unscrambled["g"]:
                    unscrambled["d"] = x
                    unscrambled["b"] = [x for x in nums[4] if x not in nums[1] and x != unscrambled["d"]][0]
    for n in data[6:9]:
        if unscrambled["d"] not in n:
            nums[0] = n
    for n in data[6:9]:
        if n != nums[0] and n != nums[9]:
            nums[6] = n
            unscrambled["c"] = [x for x in nums[8] if x not in nums[6]][0]
            unscrambled["f"] = [x for x in nums[1] if x != unscrambled["c"]][0]
    
    for n in data[3:6]:
        if nums[3] != n and unscrambled["c"] in n:
            nums[2] = n
        elif nums[3] != n and unscrambled["b"] in n:
            nums[5] = n
    
    return {nums[x] : x for x in nums}
  

if __name__ == "__main__":
    main()