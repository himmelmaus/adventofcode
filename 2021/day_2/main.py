import re

with open("input.txt") as infile:
    lines = infile.readlines()

get_changes = lambda text: sum(map(lambda x: int(x[x.rindex(" ")+1:]), filter(lambda x: text in x, lines)))
print("product: {}".format(get_changes("forward")*(get_changes("up") - get_changes("down"))))

# non code golfy part 2
#h v a
coords = [0,0,0]
for line in lines:
    if "down" in line:
        coords[2] += int(line[line.rindex(" ")+1:])
    if "up" in line:
        coords[2] -= int(line[line.rindex(" ")+1:])
    if "forward" in line:
        n = int(line[line.rindex(" ")+1:])
        coords[0] += n
        coords[1] -= n*coords[2]
print(f"final coords: ({coords[0]}, {coords[1]}), product: {coords[0]*coords[1]}")
