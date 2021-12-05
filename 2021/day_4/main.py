import numpy as np

with open("test_input.txt") as infile:
    lines = infile.read()

attempts = list(map(int, lines.split("\n\n")[0].split(",")))
print(attempts)

raw_boards = list(filter(lambda x: x != "", lines.split("\n")[1:]))
# print(raw_boards)
raw_boards = list(map(lambda x: np.array(list(map(int, filter(lambda x: x != "", x.split(" "))))), raw_boards))
# print(raw_boards)



original_boards = []

for i in range(0, len(raw_boards), 5):
    original_boards.append(raw_boards[i:i+5])

boards = np.ndarray((len(original_boards), 5, 5), dtype=int)
for i in range(len(boards)):
    for j in range(5):
        # print("j", j, original_boards[i][j], original_boards[i])
        for k in range(5):
            boards[i][j][k] = original_boards[i][j][k]

canary = 0
for attempt in attempts:
    print(attempt, type(attempt), boards.dtype)
    boards[boards == attempt] = -1
    print(boards[boards == attempt])
    for i in range(len(boards)):
        if [-1,-1,-1,-1,-1] in boards[i].tolist() or [-1,-1,-1,-1,-1] in boards[i].T.tolist():
            print(original_boards[i])
            canary = -1
            break
    if canary == -1:
        board = boards[i]
        board[board == -1] = 0
        print(sum(sum(board))*attempt)
        break

# part 2
print("part 2")
counter = 0
completed = []
completed_is = []
for ix, attempt in enumerate(attempts):
    print(ix, attempt)

    boards[boards == attempt] = -1

    for i in range(len(boards)):
        if i not in completed_is and [-1,-1,-1,-1,-1] in boards[i].tolist() or [-1,-1,-1,-1,-1] in boards[i].T.tolist():
            # print(original_boards[i])
            counter += 1
            completed_is.append(i)
            completed.append((ix, i, np.copy(boards[i])))

    print(counter, ix, len(boards), len(completed), len(list(attempts)))
    # if len(completed) == len(boards) - 1:
    #     print("hello")
    #     board = boards[i]
    #     print(board)
    #     board[board == -1] = 0
    #     print(sum(sum(board))*attempt)
    #     break

original_boards = []

for i in range(0, len(raw_boards), 5):
    original_boards.append(raw_boards[i:i+5])

boards = np.ndarray((len(original_boards), 5, 5), dtype=int)
for i in range(len(boards)):
    for j in range(5):
        # print("j", j, original_boards[i][j], original_boards[i])
        for k in range(5):
            boards[i][j][k] = original_boards[i][j][k]

print(completed)
print("hello")
board = boards[completed[-1][1]]
for ix, attempt in enumerate(attempts):
    print(ix, attempt)
    board[board == attempt] = -1
    print(board, attempt)

    if [-1,-1,-1,-1,-1] in board.tolist() or [-1,-1,-1,-1,-1] in board.T.tolist():
        # print(original_boards[i])
        # counter += 1
        # completed_is.append(i)
        # completed.append((ix, i, np.copy(boards[i])))
        break

print(board)
board[board == -1] = 0
print(sum(sum(board))*attempts[completed[-1][0]])
