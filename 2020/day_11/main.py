from copy import deepcopy

lines = list(map(lambda x: list(x.strip("\n")), open("input.txt", "r").readlines()))

flatten = lambda xs: [el for x in xs for el in x]

def mutate(lines):
    lines = deepcopy(lines)
    copied_lines = deepcopy(lines)
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if copied_lines[i][j] != ".":
                adjacent = task2_adjacent(copied_lines, i, j)
                if copied_lines[i][j] == "L" and "#" not in adjacent:
                    lines[i][j] = "#"
                    continue
                elif copied_lines[i][j] == "#" and adjacent.count("#") >= 5:
                    lines[i][j] = "L"
                    continue
    return lines

def horizontal_traverse(lines, i, j, direction):
    k = j + direction
    while k > 0 and k < len(lines) and lines[i][k] not in ["#", "L"] :
        k += direction
    if k < 0 or k >= len(lines[0]):
        return None
    if lines[i][k] in ["#", "L"]:
        return lines[i][k]
    return None
def vertical_traverse(lines,i,j,direction):
    k = i + direction
    while k > 0 and k < len(lines) and lines[k][j] not in ["#", "L"] :
        k += direction
    if k < 0 or k >= len(lines):
        return None
    if lines[k][j] in ["#", "L"]:
        return lines[k][j]
    return None
def diagonal_traverse(lines,i,j, vert_direction, hor_direction):
    m = i + vert_direction
    n = j + hor_direction
    if (m < 0 or m >= len(lines)) or (n < 0 or n >= len(lines[0])):
        return None
    while (m > 0 and m < len(lines)) and (n > 0 and n < len(lines[0])) and lines[m][n] not in ["#", "L"]:
        m += vert_direction
        n += hor_direction
    if (m < 0 or m >= len(lines)) or (n < 0 or n >= len(lines[0])):
        return None
    if lines[m][n] in ["#", "L"]:
        return lines[m][n]
    return None

def task2_adjacent(lines, i, j):

    res = list(filter(lambda x:x is not None, [
        horizontal_traverse(lines,i,j,1), horizontal_traverse(lines,i,j,-1),
        vertical_traverse(lines,i,j,1), vertical_traverse(lines,i,j,-1),
        diagonal_traverse(lines,i,j,1, -1), diagonal_traverse(lines,i,j,-1, -1),
        diagonal_traverse(lines,i,j,1,1), diagonal_traverse(lines,i,j,-1,1),
    ]))

    return res

def get_adjacent(lines, i, j):
    if i == 0:
        i_slice = [None, lines[i], lines[i+1]]
    elif i == len(lines) - 1:
        i_slice = [lines[i-1], lines[i], None]
    else:
        i_slice = [lines[i-1], lines[i], lines[i+1]]

    res = []
    if j == 0:
        for k, line in enumerate(i_slice):
            if k != 1 and line is not None:
                res.extend(line[j:j+2])
            elif k == 1:
                res.append(line[j+1])
    elif j == len(lines[0]) - 1:
        for k, line in enumerate(i_slice):
            if k != 1 and line is not None:
                res.extend(line[j-1:j+1])
            elif k == 1:
                res.append(line[j-1])
    else:
        for k, line in enumerate(i_slice):
            if k != 1 and line is not None:
                res.extend(line[j-1:j+2])
            elif k == 1:
                res.append(line[j-1])
                res.append(line[j+1])
    # print(res)
    return res

line_changes = [lines, mutate(mutate(lines))]

from time import time

t1 = time()

while flatten(line_changes[-1]) != flatten(line_changes[-2]):
    line_changes.append(mutate(line_changes[-1]))

print([el for line in line_changes[-1] for el in line].count("#"))
print("Completed in ", time()-t1, "s")