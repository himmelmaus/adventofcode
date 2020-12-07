with open("input.txt", "r") as infile:
    lines = list(map(lambda x: x.strip("\n"), infile.readlines()))

import re

types = list(set([line.split("bags")[0] for line in lines]))

tree = {typ: [] for typ in types}

bag_counts = {}

regex = re.compile("\d+")


for line in lines:
    tree[line.split("bags")[0]] = [typ for typ in types if typ in line.split("contain")[1]]
    key = line.split("bags")[0]
    addition = {}
    for fragment in line.split("contain")[1].strip(" ").strip(".").split(","):
        fragment = fragment.split(" ")
        if "" in fragment:
            del fragment[fragment.index("")]
        addition[" ".join(fragment[1:3]) + " "] = 0 if "no" in fragment else int(fragment[0])
        print(fragment)
    bag_counts[key] = addition

print(bag_counts)


def find_shiny_gold(key):
    if "shiny gold " in tree[key]:
        return True
    res = False
    for key2 in tree[key]:
        if find_shiny_gold(key2):
            return True
    return False

def count_shiny_gold(key):
    res = 0
    for key2 in bag_counts[key]:
        try:
            res += bag_counts[key][key2]*(1 + count_shiny_gold(key2))
        except:
            print(key, key2)
            continue
    return res

shiny_count = 0
for key in tree:
    if find_shiny_gold(key):
        shiny_count += 1
print(count_shiny_gold("shiny gold "))