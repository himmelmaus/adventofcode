lines = list(open("input.txt").readlines())

target_time = int(lines[0])
filtered_times = lines[1].strip().split(",")
buses = [[int(bus), filtered_times.index(bus)] for bus in filtered_times if bus != "x"]

print(buses)

time = target_time
canary = False

# part 1
while True:
    for bus, _ in buses:
        if time%bus == 0:
            canary = True
            print("Earliest time to depart ", time)
            print("Final output ", (time-target_time) * bus)
            break
    if canary:
        break
    time += 1

# part 2
canary = False
from time import time as ti
t1 = ti()
time = 1
times = []

def product(xs):
    product = 1
    for x in xs:
        product *= x
    return product

for i, bus in enumerate(buses):
    while (time + product([bus[1] for bus in buses[:i+1]]))%bus[0] != 0:
        time += 1
    times.append(time)
    continue

# product = 1
# for time in times:
#     product *= time
print(sum(times))
    # if time%buses[3][0] == 0:
    #     canary = True
    #     for bus in buses:
    #         if not (time + bus[1])%bus[0] == 0:
    #             canary = False
    #             break
    #     if canary:
    #         print("Earliest time to depart in sequence", time)
    #         break
    # if time%1000000 == 0:
    #     print(time, " ", ti() - t1, "s")
    # time -= 1