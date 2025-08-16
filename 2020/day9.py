def main():
    
    data = parseInput("input.txt")
    preamble = 25

    part1 = 0
    for i in range(preamble, len(data)):
        if not isValid(data[i], data[i - preamble:i]):
            part1 = data[i]
            break
    print(part1)

    for i in range(len(data)):
        x = data[i]
        buffer = [x]
        j = i + 1
        while x <= part1:
            x += data[j]
            buffer.append(data[j])
            if x == part1:
                buffer.sort()
                print(buffer[0] + buffer[-1])
                return
            j += 1


def parseInput(f):
    with open(f) as file:
        return [int(x.strip()) for x in file]
    

def isValid(x, nums):

    for i, n in enumerate(nums):
        if x - n in nums[i + 1:]:
            return True
        
    return False
    

if __name__ == "__main__":
    main()