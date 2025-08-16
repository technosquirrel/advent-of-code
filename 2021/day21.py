from itertools import product

def main():
    
    players = [{"square" : 5, "score" : 0}, {"square" : 6, "score" : 0}]

    i = 0
    dice = 1
    rolls = 0
    while True:
        n = (dice * 3 + 3) % 10
        dice += 3
        rolls += 3
        players[i]["square"] += n
        if players[i]["square"] > 10:
            players[i]["square"] -= 10
        players[i]["score"] += players[i]["square"]
        i = 1 - i
        if players[1 - i]["score"] >= 1000:
            print(players[i]["score"] * rolls)
            break


    scoreTable = calculatePossibilities([1, 2, 3])
    winners = [0, 0]
    games = {((5, 0), (6, 0)) : 1}

    i = 0

    while len(games) > 0:
        newGames = {}
        for game in games:
            for score in scoreTable:
                tmp = [x for x in game[i]]
                tmp[0] += score
                if tmp[0] > 10:
                    tmp[0] -= 10
                tmp[1] += tmp[0]
                if tmp[1] >= 21:
                    winners[i] += games[game] * scoreTable[score]
                else:
                    newGame = [0, 0]
                    newGame[i] = tuple(x for x in tmp)
                    newGame[1 - i] = tuple(x for x in game[1 - i])
                    newGame = tuple(newGame)
                    try:
                        newGames[newGame] += games[game] * scoreTable[score]
                    except:
                        newGames[newGame] = games[game] * scoreTable[score]
        games = newGames     
        i = 1 - i

    winners.sort()
    print(winners[-1])

def calculatePossibilities(i):

    tmp = list(product(i, repeat=len(i)))
    possibilities = {}

    for k in tmp:
        try:
            possibilities[sum(k)] += 1
        except:
            possibilities[sum(k)] = 1

    return possibilities


if __name__ == "__main__":
    main()