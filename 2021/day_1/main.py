import csv, itertools, functools, math

with open("./input.txt") as infile:
    lines = infile.readlines()

lines = [int(val) for val in lines]

greater = []

for i in range(len(lines)-1):
    greater.append(int(lines[i+1] > lines[i]) )

lines = lines

counter = 1
tups = []
# for i in range(-2, len(lines)):
#     if i < 0:
#         it = 0
#         jit=i+3
#     elif i >= len(lines)-2:
#         it=i
#         jit=len(lines)
#     else:
#         it=i
#         jit=i+3
#     tups.append((it,jit))

greater = []

for i in range(0, len(lines)):
    # l = tups[i]
    # g = tups[i+1]
    # print(lines[g[0]:g[1]], sum(lines[g[0]:g[1]]), lines[l[0]:l[1]], sum(lines[l[0]:l[1]]), " : ", int(sum(lines[g[0]:g[1]]) > sum(lines[l[0]:l[1]])))

    # greater.append(int(sum(lines[g[0]:g[1]]) > sum(lines[l[0]:l[1]])))

    greater.append(int(sum(lines[i+1:i+4])>sum(lines[i:i+3])))


print(sum(greater))