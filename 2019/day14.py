class Node:
    def __init__(self, name, x, reagents):
        self.name = name
        self.quantity = x
        self.reagents = reagents


def main():

    input = parseInput("test.txt")
    factory = makeTree("FUEL", input, {})

    print(getCost(factory, {}))


def parseInput(f):

    reactions = {}

    with open(f) as file:
        for line in file:
            line = line.strip().split(" => ")
            n = line[1].split()
            reactions[n[1]] = {"quantity" : int(n[0]), "reagents" : [x.split() for x in line[0].strip().split(", ")]}

    return reactions


def makeTree(start, input, nodes):
    
    if start in nodes:
        return nodes[start]
    else:
        if start not in input:
            return Node(start, 1, [])
        else:
            reagents = {}
            for reagent in input[start]["reagents"]:
                reagents[reagent[1]] = {"node" : makeTree(reagent[1], input, nodes), "quantity" : int(reagent[0])}
            n = Node(start, input[start]["quantity"], reagents)
            nodes[start] = n
            return n


def getCost(node, leftovers):
    
    for reagent in node.reagents:
        if not node.reagents[reagent]["node"].reagents:
            return node.reagents[reagent]["quantity"]
        


if __name__ == "__main__":
    main()