from functools import cache
import time

def main():
    
    start = time.time()
    stones = parseInput("input.txt")
    stones = {stone : 1 for stone in stones}
    
    for _ in range(1000):
        newStones = {}
        for stone in stones:
            buffer = blink(stone)
            for s in buffer:
                try:
                    newStones[s] += stones[stone]
                except:
                    newStones[s] = stones[stone]
        stones = newStones
    
    print(sum(stones.values()))
    print(time.time() - start)


def parseInput(f):
    with open(f) as file:
        return [int(x) for x in file.readline().split()]
    

@cache
def blink(x):

    if x == 0:
        return [1]
    else:
        n = str(x)
        l = len(n)
        if l % 2 == 0:
            return [int(n[:l//2]), int(n[l//2:])]
        else:
            return [x * 2024]


if __name__ == "__main__":
    main()