with open("input.txt", "r") as infile:
    lines = list(map(lambda x: x.strip("\n"), infile.readlines()))

def get_row(id):
    rows = list(range(0, 128))
    for char in id:
        split = int(len(rows)/2)
        if char == "F":
            rows = rows[:split]
        else:
            rows = rows[split:]
    return rows[0]

def get_column(id):
    rows = list(range(0, 8))
    for char in id:
        split = int(len(rows)/2)
        if char == "L":
            rows = rows[:split]
        else:
            rows = rows[split:]
    return rows[0]

def get_seat_ids(lines):
    seat_ids = []
    for line in lines:
        seat_id = get_row(line[:7]) * 8 + get_column(line[7:])
        seat_ids.append(seat_id)
    return seat_ids

def task1(lines):
    return max(get_seat_ids(lines))

def task2(lines):
    seat_ids = get_seat_ids(lines)
    seat_ids.sort()
    for i in range(max(seat_ids)):
        # This would be nicer with if statements but I'm an eejit
        try:
            index = seat_ids.index(i)
            continue
        except ValueError:
            try:
                seat_ids.index(i-1)
                seat_ids.index(i+1)
            except ValueError:
                continue
            return i

print(task2(lines))