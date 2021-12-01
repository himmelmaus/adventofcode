import numpy as np
from copy import deepcopy

lines = list(map(lambda x: [x[0], int(x[1:].strip())], open("input.txt", "r").readlines()))

position = [0, 0]

direction = 90

def direction_vector(direction):
    direction = direction%360
    if direction == 0:
        return [1, 0]
    elif direction == 90:
        return [0,1]
    elif direction == 180:
        return [-1, 0]
    elif direction == 270:
        return [0, -1]
    
    

for command, value in lines:
    if command == "N":
        position[0] += value
    if command == "S":
        position[0] -= value
    if command == "E":
        position[1] += value
    if command == "W":
        position[1] -= value
    if command == "L":
        direction -= value
    if command == "R":
        direction += value
    if command == "F":
        dir_vec = direction_vector(direction)
        for i in range(len(position)):
            position[i] += dir_vec[i]*value


#part 2
position = np.array([0.0, 0.0])
rel_vec = np.array([1.0, 10.0])

direction = 90

def rotate_waypoint(angle, rel_vec):
    theta = 2*np.pi*(angle/360)
    rel_vec = deepcopy(rel_vec)
    rot_vec = np.array(
        [
            rel_vec[0]*np.cos(theta) - rel_vec[1]*np.sin(theta),
            rel_vec[0]*np.sin(theta) + rel_vec[1]*np.cos(theta)
        ]
    )
    return deepcopy(rot_vec)
    
    

for command, value in lines:
    if command == "N":
        rel_vec[0] += value
    if command == "S":
        rel_vec[0] -= value
    if command == "E":
        rel_vec[1] += value
    if command == "W":
        rel_vec[1] -= value
    if command == "L":
        rel_vec = rotate_waypoint(-value, rel_vec)
    if command == "R":
        rel_vec = rotate_waypoint(value, rel_vec)
    if command == "F":
        position += value*rel_vec

    print(position, rel_vec, command, value)


print(position, direction, sum([np.abs(pos) for pos in position]))