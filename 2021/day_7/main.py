from functools import reduce
import numpy as np

crabbies = np.array(list(map(int, open("test_input.txt").read().split(","))))

print("part 1")
print(min(map(lambda x: sum(np.abs(crabbies - x)), range(0, max(crabbies)))))

print("part 2")
print(min(map(lambda x: sum(map(lambda x: sum(range(x+1)), np.abs(crabbies - x))), range(0, max(crabbies)))))
