with open("input.txt", "r") as infile:
    lines = infile.read().split("\n\n")

total_count = 0
for line in lines:
    total_count += sum([1 for character in "abcdefghijklmnopqrstuvwxyz" if all([character in subline for subline in line.split("\n")])])
print(total_count)