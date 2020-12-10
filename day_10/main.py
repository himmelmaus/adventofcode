from copy import deepcopy
import itertools
import numpy as np

lines = list(map(lambda x: int(x.strip("\n")), open("input.txt", "r").readlines()))
lines.sort()
lines = [0] + lines

num_1s = 0
num_3s = 0
used_adapters = lines
for i in range(0, len(used_adapters)-1):
    if np.abs(used_adapters[i] - used_adapters[i+1]) == 1:
        num_1s += 1
    if np.abs(used_adapters[i] - used_adapters[i+1]) == 3:
        num_3s += 1

print(num_1s*(num_3s+1))

def is_valid(arrangement):
    for i in range(1, len(arrangement)):
        if arrangement[i] - arrangement[i-1] > 3:
            return False
    return True

def get_partitions(lines):
    # Due to the constraints, any differences between adapters of > 3 can't be removed
    # So the number of permutations can be massively cut down by only considering
    # the permutations of values between the 3-gaps in the list
    last_index = 0
    index = 1
    partitions = []
    while index < len(lines) + 1:
        while index < len(lines) - 1 and lines[index] - lines[index - 1] < 3:
            index += 1
        partitions.append(lines[last_index:index])
        last_index= index
        index = last_index + 1

    return partitions

lines.append(max(lines) + 3)
partitions = get_partitions(lines)
running_total = 1
for partition in partitions:

    if len(partition) > 2:
        total = 0

        perms = [list(itertools.combinations(partition[1:-1],i)) for i in range(len(partition))]
        perms = [list(perm) for sublist in perms for perm in sublist]

        for perm in perms:
            if is_valid(partition[:1] + perm + partition[-1:]):
                total += 1

        if total != 0:
            running_total *= total

print(lines, "\n", partitions, "\n", running_total)