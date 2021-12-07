from functools import reduce
import numpy as np


crabbies = np.array(list(map(int, open("input.txt").read().split(","))))
positions = np.array(range(0, max(crabbies)))


print("part 1")
print(min(map(lambda x: sum(np.abs(crabbies - x)), positions)))

print("part 2")
tri_sum = lambda x: reduce(lambda a, b: a+b, range(x+1)) if x!= 0 else 0
print(min(map(lambda x: sum(map(tri_sum, np.abs(crabbies - x))), positions)))