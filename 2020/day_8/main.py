from copy import deepcopy

with open("input.txt", "r") as infile:
    lines = list(infile.readlines())

tokenised = [[line[:3], int(line[4:])] for line in lines]

def get_total(lines):
    accumulator = 0
    i = 0
    executed = []
    while True:

        if i in executed:
            return None

        executed.append(i)

        if lines[i][0] == "acc":
            accumulator += lines[i][1]
            i += 1

        elif lines[i][0] == "jmp":
            i += lines[i][1]

        else:
            i += 1

        if i >= len(lines) - 1:
            return accumulator

    return accumulator


for i in range(len(tokenised)):
    copied_lines = deepcopy([deepcopy([deepcopy(tok) for tok in token]) for token in tokenised])

    if copied_lines[i][0] == "acc":
        continue

    if copied_lines[i][0] == "jmp":
        copied_lines[i][0] = "nop"

    elif copied_lines[i][0] == "nop":
        copied_lines[i][0] = "jmp"

    print(tokenised[i] == copied_lines[i])
    accumulator = get_total(copied_lines)
    
    if accumulator is not None:
        print("I think this is it", accumulator)
        break

