with open("input.txt") as infile:
    lines = list(infile.readlines())
    lines=[line.strip('\n') for line in lines]
    running_count = 1
    for i in [1,3,5,7]:
        trees = 0
        counter = -i
        for line in lines:
            copy_line = list(line)
            counter = (counter + i)%len(line)
            if line[counter] == "#":
                trees += 1
        print(i, trees)
        running_count *= trees
    trees = 0
    counter = -1
    for j, line in enumerate(lines):
        if j%2 == 0:
            copy_line = list(line)
            counter = (counter + 1)%len(line)
            if line[counter] == "#":
                trees += 1
                copy_line[counter] = "X"
            else:
                copy_line[counter] = "O"
    running_count *= trees
    print(running_count)