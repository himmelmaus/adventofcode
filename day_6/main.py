with open("input.txt", "r") as infile:
    lines = infile.read().split("\n\n")


count1 = sum([sum([1 for character in "abcdefghijklmnopqrstuvwxyz" if character in line]) for line in lines])
count2 = sum([sum([1 for character in "abcdefghijklmnopqrstuvwxyz" if all([character in subline for subline in line.split("\n")])]) for line in lines])

print(count1, count2)