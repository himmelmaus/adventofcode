import numpy as np

with open("input.txt") as infile:
    original_fishies = np.array(list(map(int, infile.read().split(","))))

fishies = np.array(original_fishies)
for i in range(80):
    print(f"iteration {i}, {len(fishies)} fishies")
    fishies -= 1
    pregnant_fishies = fishies == -1
    new_fishies = np.count_nonzero(pregnant_fishies)
    fishies[pregnant_fishies] = 6
    fishies = np.append(fishies, [8]*new_fishies)
    # print(fishies)

print(len(fishies))

# part 2

fishies = {x:np.count_nonzero(original_fishies == x) for x in range(9)}
for i in range(256):
    print(fishies)
    for i in range(9):
        fishies[i-1] = fishies[i]
    fishies[8] = fishies[-1]
    fishies[6] += fishies[-1]
    del fishies[-1]
    
print(sum(fishies.values()))
