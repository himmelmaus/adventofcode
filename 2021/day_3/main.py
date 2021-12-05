
# document.getElementsByTagName("body")[0].textContent
import statistics

with open(" input.txt") as infile:
    lines = infile.readlines()

avgs = []
most_bits = []
least_bits = []

for i in range(len(lines[0].strip("\n"))):
    ints = [int(line.strip("\n")[i]) for line in lines]
    avgs.append(sum(ints)/(len(ints)))


for avg in avgs:
    if avg >= 0.5:
        most_bits.append(1)
        least_bits.append(0)
    else:
        most_bits.append(0)
        least_bits.append(1)

print(int("".join(map(str, most_bits)),2)*int("".join(map(str,least_bits)),2))

map(    )

most_common = []
for i in range(len(lines[0].strip("\n"))):
    ints = [int(line.strip("\n")[i]) for line in lines]
    ints.sort()
    ints.reverse()
    most_common.append(statistics.mode(ints))

def bit_criteria(lines, m):
    lines = [line.strip("\n") for line in list(lines)]
    pos = -1
    print(lines)
    while len(lines) > 1:
        pos += 1
        print(pos, lines)
        ints = [int(line.strip("\n")[pos]) for line in lines]
        ints.sort()
        ints.reverse()
        most_common = statistics.mode(ints)
        if m == 1:
            print(pos, most_common)
            if most_common == 1:
                lines = list(filter(lambda x: x[pos] == "1", lines ))
            else:
                lines = list(filter(lambda x: x[pos] == "0", lines ))
        else:
            if most_common == 1:
                lines = list(filter(lambda x: x[pos] == "0", lines ))
            else:
                lines = list(filter(lambda x: x[pos] == "1", lines ))
        print(pos, lines)
        if len(lines) == 1:
            return lines[0]
    return lines[0]


print(avgs)
lines_backup = list(lines)
o2 = bit_criteria(lines_backup, 1)
co2 = bit_criteria(lines_backup, 0)
print(int(o2, 2), int(co2, 2))
print((int("".join(map(str, o2)),2))*int("".join(map(str,co2)),2))