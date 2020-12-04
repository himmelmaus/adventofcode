import re

with open("input.txt") as infile:
    input = infile.read()

fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]

lines = input.split("\n\n")
def task1():
    count = 0
    for line in lines:
        if all([field in line for field in fields if field != "cid"]):
            count += 1
    print(count)

def check(key, value):
    print(key, value)
    if key == "byr":
        return len(value) == 4 and int(value) >= 1920 and int(value) <= 2002
    if key == "iyr":
        return len(value) == 4 and int(value) >= 2010 and int(value) <= 2020
    if key == "eyr":
        return len(value) == 4 and int(value) >= 2020 and int(value) <= 2030
    if key == "hgt":
        return (value[-2:] == "cm" and int(value[:-2]) >= 150 and int(value[:-2]) <= 193) or (value[-2:] == "in" and int(value[:-2]) >= 59 and int(value[:-2]) <= 76)
    if key == "ecl":
        return sum([value == typ for typ in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]]) == 1
    if key == "pid":
        return len(value) == 9 and value.isnumeric()
    if key == "hcl":
        return re.compile("^#([0-9]|[a-f]){6}$").search(value)
    if key == "cid":
        return True
def task2():
    count = 0
    lines = input.split("\n\n")
    # print(lines)
    for line in lines:
        canary = True
        line = line.replace("\n", " ")
        print([line])
        if all([field in line for field in fields if field != "cid"]):
            values = line.replace("\n", " ").split(" ")
            # print(" ".join(values))
            for value in values:
                if not check(*value.split(":")):
                    canary = False
                    break
            if canary:
                print(line)
                count += 1
            print("\n")
    print(count)

task2()