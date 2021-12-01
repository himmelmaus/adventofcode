with open("./input.txt") as infile:
    lines = infile.readlines()

def part_1(lines):
    valid_count = 0
    for line in lines:
        lower = int(line.split("-")[0])
        upper = int(line.split("-")[1].split(" ")[0])
        letter = str(line.split(":")[0][-1])
        password = str(line.split(":")[1])
        if password.count(letter) >= lower and password.count(letter) <= upper:
            valid_count += 1
    return valid_count

valid_count = part_1(lines)
print(valid_count)

def part_2(lines):
    valid_count = 0
    for line in lines:
        lower = int(line.split("-")[0])
        upper = int(line.split("-")[1].split(" ")[0])
        letter = str(line.split(":")[0][-1])
        password = str(line.split(":")[1])
        if (password[lower] == letter and password[upper] != letter) or (password[lower] != letter and password[upper] == letter):
            valid_count += 1
    return valid_count

valid_count = part_2(lines)
print(valid_count)