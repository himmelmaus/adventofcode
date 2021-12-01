lines = list(map(lambda x: int(x.strip("\n")), open("input.txt", "r").readlines()))

def adds(options, target):
    return len([1 for x in options for y in options if x + y == target]) > 0

for i in range(25, len(lines)):
    if not adds(lines[i-25:i], lines[i]):
        print(lines[i])

for i in range(len(lines)):
    j = i + 1
    while sum(lines[i:j]) < 731031916:
        j += 1
    if sum(lines[i:j]) == 731031916:
        print(min(lines[i:j]) + max(lines[i:j]))
        break