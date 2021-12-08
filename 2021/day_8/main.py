import numpy as np

with open("input.txt") as infile:
    lines = list(map(lambda x: x.split("|"), infile.read().splitlines()))
signals = []

for line in lines:
    signals.append([signal.strip().split(" ") for signal in line])

outputs = [signal[1] for signal in signals]
outputs = np.array(outputs).flatten()

print(len(list(filter(lambda x: len(x) in [2, 3, 4, 7], outputs))))

# part 2
# each index has the set of segments turned on for it
true_mappings = ["abcefg", "cf", "acdeg", "acdfg", "bcdf", "abdfg", "abdefg", "acf", "abcdefg", "abcdfg"]
rolling_sum = 0
for (signal, output) in signals:
    mappings = {}
    unassigned = ["a", "b", "c", "d", "e", "f", "g"]

    # string values
    one = list(filter(lambda x: len(x) == 2, signal))[0]
    four = list(filter(lambda x: len(x) == 4, signal))[0]
    seven = list(filter(lambda x: len(x) == 3, signal))[0]
    eight = list(filter(lambda x: len(x) == 7, signal))[0]

    zero_six_or_nine = list(filter(lambda x: len(x) == 6, signal))
    two_three_or_five = list(filter(lambda x: len(x) == 5, signal))



    mappings["a"] = list(set(seven) - set(one))[0]
    unassigned.remove(mappings["a"])
    for val in zero_six_or_nine:
        # only 6 doesn't cover c, the rest cover both
        if len(list(set(one) - set(val))) != 0:
            mappings["c"] = list(set(one) - set(val))[0]
            unassigned.remove(mappings["c"])
    # one contains c and f, ergo one - c = f
    mappings["f"] = list(filter(lambda x: x != mappings["c"], list(one)))[0]
    unassigned.remove(mappings["f"])

    b_or_d = set(four) - {mappings["c"], mappings["f"]}

    for val in b_or_d:
        # d is in all of them, b is only in five
        if len(list(filter(lambda x: val in x, two_three_or_five))) == 1:

            mappings["b"] = val
            unassigned.remove(mappings["b"])

            mappings["d"] = list(b_or_d - {mappings["b"]})[0]
            unassigned.remove(mappings["d"])

            five = set(list(filter(lambda x: mappings["b"] in x, two_three_or_five))[0])
            mappings["g"] = list(five - set(mappings.values()))[0]
            print("g", mappings["g"], unassigned)
            unassigned.remove(mappings["g"])

            # only value left
            mappings["e"] = unassigned[0]
            # just for closure
            unassigned.remove(mappings["e"])
            assert len(unassigned) == 0

    inverted_mappings = {val: key for key, val in mappings.items()}

    decoded = []
    for value in true_mappings:
        decoded.append(set([mappings[val] for val in list(value)]))

    print(mappings, "\n", inverted_mappings, "\n",true_mappings, "\n", decoded)

    value = ""
    for output in outputs:
        value += str(decoded.index(set(output)))
    rolling_sum += int(value)
print(rolling_sum)