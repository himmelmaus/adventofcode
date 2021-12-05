import numpy as np

with open("input.txt") as infile:
    lines = map(lambda x: x.split(" ")[::2], infile.read().splitlines())
    # ((x1, y1), (x2, y2))
    lines = [[x.split(",") for x in line] for line in lines]
    # ((x1, x2), (y1, y2))
    coords = [((int(x1), int(x2)), (int(y1), int(y2))) for ((x1, y1), (x2, y2)) in lines]

straight_verticals = filter(lambda x: x[1][0] == x[1][1], coords)
straight_horizontals = filter(lambda x: x[0][0] == x[0][1], coords)

diagonals = filter(lambda x: x[0][0] != x[0][1] and x[1][0] != x[1][1], coords)

flattened_xs = [x for coord_set in coords for x in coord_set[0]]
flattened_ys = [y for coord_set in coords for y in coord_set[1]]

line_map = np.zeros((max(flattened_xs)+1, max(flattened_ys)+1))

for ((x1, x2), (y1, y2)) in straight_verticals:
    y = y1
    x_dir = (x2 - x1)
    x_dir = int(x_dir/abs(x_dir))
    for x in range(x1, x2+x_dir, x_dir):
        print(x,y)
        line_map[x][y] += 1

for ((x1, x2), (y1, y2)) in straight_horizontals:
    x = x1
    y_dir = (y2 - y1)
    y_dir = int(y_dir/abs(y_dir))
    # print(vec)
    for y in range(y1, y2+y_dir, y_dir):
        # print(x,y)
        line_map[x][y] += 1

cond = line_map >= 2
print(line_map)
print(np.count_nonzero(cond))

print("part 2")

for ((x1, x2), (y1, y2)) in diagonals:
    x = x1
    y = y1
    try:
        y_dir = (y2 - y1)    
        y_dir = int(y_dir/abs(y_dir))
    except ZeroDivisionError:
        y_dir = 1

    try:
        x_dir = (x2 - x1)
        x_dir = int(x_dir/abs(x_dir))
    except ZeroDivisionError:
        x_dir = 1

    while y2 + y_dir - y != 0 and x2 + x_dir - x != 0:
        line_map[x][y] += 1
        x += x_dir
        y += y_dir

cond = line_map >= 2
print(line_map)
print(np.count_nonzero(cond))