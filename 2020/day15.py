import time

def main():

    start = time.time()
    nums = parseInput("input.txt")
    
    print(playGame(nums, 30000000))
    print(time.time() - start)


def parseInput(f):
    with open(f) as file:
        return [int(x) for x in file.readline().strip().split(",")]


def playGame(nums, l):

    cache = {x : i + 1 for i, x in enumerate(nums[:-1])}
    i = len(nums) + 1
    lastX = nums[-1]

    while i <= l:
        try:
            n = i - 1 - cache[lastX]
            cache[lastX] = i - 1
            lastX = n
        except:
            cache[lastX] = i - 1
            lastX = 0
        i += 1

    return lastX

if __name__ == "__main__":
    main()