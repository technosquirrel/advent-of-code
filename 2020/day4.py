import re

def main():

    passports = parseInput("input.txt")

    l = 8
    optional = "cid"

    valid = []
    for passport in passports:
        if len(passport) == l or (len(passport) == l - 1 and optional not in passport):
            valid.append(passport)
    print(len(valid))


    part2 = 0
    for passport in valid:
        if isValid(passport):
            part2 += 1
    print(part2)


def parseInput(f):

    passports = []

    with open(f) as file:
        passport = {}
        for line in file:
            line = line.strip().split()
            if not line:
                passports.append(passport)
                passport = {}
            else:
                for n in line:
                    n = n.split(":")
                    passport[n[0]] = n[1]

    if passport:
        passports.append(passport)

    return passports


def isValid(passport):

    try:
        x = int(passport["byr"])
        if x < 1920 or x > 2002:
            return False
    except:
        return False
    
    try:
        x = int(passport["iyr"])
        if x < 2010 or x > 2020:
            return False
    except:
        return False
    
    try:
        x = int(passport["eyr"])
        if x < 2020 or x > 2030:
            return False
    except:
        return False
    
    m = re.search(r"^(\d+)(in|cm)$", passport["hgt"])
    if not m:
        return False
    if m[2] == "cm":
        if int(m[1]) < 150 or int(m[1]) > 193:
            return False
    elif m[2] == "in":
        if int(m[1]) < 59 or int(m[1]) > 76:
            return False
        
    m = re.search(r"^#[\da-f]{6}$", passport["hcl"])
    if not m:
        return False
    
    if passport["ecl"] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        return False
    
    m = re.search(r"^\d{9}$", passport["pid"])
    if not m:
        return False
    
    return True


if __name__ == "__main__":
    main()