def runIntcode(program, inputs=None, base=0, pos=0, output=[]):

    if type(program) == list:
        copy = {i : x for i, x in enumerate(program)}
    else:
        copy = program
    pos = 0
    base = base
    output = output

    inputs = inputs
    
    while True:
        outs = runInstruction(copy, pos, inputs, base)
        if "pos" in outs:
            pos = outs["pos"]
        else:
            return [False, copy, inputs, base, pos, output]
        if "out" in outs:
            output.append(outs["out"])
        if "halt" in outs:
            return output
        if "base" in outs:
            base = outs["base"]
        

def runLoop(program, inputs, base=0):

    copies = []
    l = len(inputs)
    
    for n in inputs:
        copies.append({
            "code" : [x for x in program],
            "pos" : 0,
            "inputs" : n,
            "output" : False,
            "base" : base
        })

    i = 0
    while True:
        outs = runInstruction(copies[i]["code"], copies[i]["pos"], copies[i]["inputs"], copies[i]["base"])
        if not "pos" in outs:
            i = (i + 1) % l
        else:
            copies[i]["pos"] = outs["pos"]
            if "out" in outs:
                copies[(i + 1) % l]["inputs"].append(outs["out"])
                copies[i]["output"] = outs["out"]
            if "halt" in outs:
                if i == l - 1:
                    return copies[i]["output"]
                else:
                    i = (i + 1) % l
            

def runInstruction(code, pos, inputs, base=0):

    opcode = str(code[pos]).zfill(5)
    if opcode[-2:] == "03":
        c = 0 if opcode[2] == "0" else base
    else:
        c = 0 if opcode[0] == "0" else base
    
    try:
        a = code[code[pos + 1]] if opcode[2] == "0" else code[pos + 1] if opcode[2] == "1" else code[code[pos + 1] + base]
    except:
        a = 0

    try:
        b = code[code[pos + 2]] if opcode[1] == "0" else code[pos + 2] if opcode[1] == "1" else code[code[pos + 2] + base]
    except:
        b = 0


    match opcode[-2:]:
        case "01":
            code[code[pos + 3] + c] = a + b
            return {"pos" : pos + 4}
        case "02":
            code[code[pos + 3] + c] = a * b
            return {"pos" : pos + 4}
        case "03":
            try:
                code[code[pos + 1] + c] = inputs[0]
                del inputs[0]
                return {"pos" : pos + 2}
            except:
                return {}
        case "04":
            return {"pos" : pos + 2, "out" : a}
        case "05":
            x = b if a != 0 else pos + 3
            return {"pos" : x}
        case "06":
            x = b if a == 0 else pos + 3
            return {"pos" : x}
        case "07":
            code[code[pos + 3] + c] = 1 if a < b else 0
            return {"pos" : pos + 4}
        case "08":
            code[code[pos + 3] + c] = 1 if a == b else 0
            return {"pos" : pos + 4}
        case "09":
            return {"pos" : pos + 2, "base" : base + a}
        case "99":
            return {"pos" : pos + 1, "halt" : True}
        case _:
            raise ValueError
        

def parseInput(f):
    with open(f) as file:
        return [int(x) for x in file.readline().strip().split(",")]