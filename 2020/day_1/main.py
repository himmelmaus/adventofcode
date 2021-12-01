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

# if __name__ == "__main__":
#     with open("./input.csv", "r") as infile:
#         rows = list(map(lambda x: int(x[0]), csv.reader(infile)))

#         product1 = part_1(2020, rows)
#         print(f"Task 1 solution: {product1}")

#         product2 = part_2(2020, rows)
#         print(f"Task 2 solution: {product2}")

# infile = open("input.txt", "r")
# input = infile.read()
# input = map(lambda x: x.strip("\n"), input)

# input = "\n".join([line + "test" for line in input])

# input = "I love you lil sunners"

# outfile = open("output.txt", "a")
# outfile.write(input)


infile = list(map(lambda x: x.strip("\n").split(" "), open("freq_en_50k.txt", "r").readlines()))

input = [(token, int(frequency)) for token, frequency in infile]

# total_word_count = sum([frequency for _, frequency in input])

# running_total_frequency = 0
# word_count = 0
# deciles = []
# threshold = 0.1

# for token, frequency in input:
#     running_total_frequency += frequency
#     word_count += 1
#     if running_total_frequency/total_word_count > threshold:
#         deciles.append(word_count)
#         threshold += 0.1

# return deciles

def task_3(input):

    def get_prefixes(word):
        letters = list(word)
        prefixes = []
        for i in range(len(letters)):
            prefixes.append("".join(letters[:i+1]))
        return prefixes

    prefix_frequencies = {}

    for token, frequency in input:
        for prefix in get_prefixes(token):
            if prefix not in prefix_frequencies:
                prefix_frequencies[prefix] = sum([frequency for token,frequency in input if token.startswith(prefix)])


    prefix_frequencies = [(key, prefix_frequencies[key]) for key in prefix_frequencies]
    prefix_frequencies.sort()

    return prefix_frequencies

def store_frequencies_alphabetically(frequencies, freq_file_name):

    with open(freq_file_name, "w") as outfile:
        frequencies.sort(key = lambda x: x[0])
        outfile.writelines(["{} {}\n".format(*tup) for tup in frequencies])

frequencies = task_3(input)
store_frequencies_alphabetically(frequencies, "test_output.txt")