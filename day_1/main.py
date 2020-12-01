import csv, itertools, functools

def part_1(target, numbers):
    for number in numbers:
        if (target - number) in numbers:
            return number*(target-number)
            
def part_2(target, numbers):
    combinations = itertools.combinations(numbers, 3)
    for combination in combinations:
        if sum(combination) == target:
            return functools.reduce((lambda a,b: a*b) , combination)

if __name__ == "__main__":
    with open("./input.csv", "r") as infile:
        rows = list(map(lambda x: int(x[0]), csv.reader(infile)))

        product1 = part_1(2020, rows)
        print(f"Task 1 solution: {product1}")

        product2 = part_2(2020, rows)
        print(f"Task 2 solution: {product2}")