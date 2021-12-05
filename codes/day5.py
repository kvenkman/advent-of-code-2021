from collections import defaultdict

test = False

if test:
    input = '../inputs/day5_test'
else:
    input = '../inputs/day5_input'

with open(input, 'r') as f:
    lines = f.readlines()

def generate_vent(start, end):
    vent = []
    increment = None
    
    # Horizontal and vertical lines
    if start[0] == end[0]:
        increment = (0, 1) if end[1] > start[1] else (0, -1)
    if start[1] == end[1]:
        increment = (1, 0) if end[0] > start[0] else (-1, 0)
    
    if not increment:
        return vent
    
    while start != end:
        vent.append(tuple(start))
        start[0] += increment[0]
        start[1] += increment[1]
    vent.append(tuple(start))

    return vent

def generate_vent_diagonals(start, end):
    vent = []
    increment = None
    
    # Horizontal and vertical lines
    if start[0] == end[0]:
        increment = (0, 1) if end[1] > start[1] else (0, -1)
    if start[1] == end[1]:
        increment = (1, 0) if end[0] > start[0] else (-1, 0)

    # Diagonal lines
    if (start[0] - end[0]) and (start[1] - end[1]):
        if start[0] > end[0]:
            increment = (-1, 1) if start[1] < end[1] else (-1, -1)
        else:
            increment = (1, 1) if start[1] < end[1] else (1, -1)
    
    if not increment:
        return vent
    
    while start != end:
        vent.append(tuple(start))
        start[0] += increment[0]
        start[1] += increment[1]
    vent.append(tuple(start))

    return vent

# Part 1
ocean_floor = defaultdict(int)
for l in lines:
    coordinates = l.strip().split('->')
    start = [int(p) for p in coordinates[0].split(',')]
    end = [int(p) for p in coordinates[1].split(',')]
    
    vent = generate_vent(start, end)
    # print(vent)
    for p in vent:
        ocean_floor[p] += 1

n_overlap = 0
for _, v in ocean_floor.items():
    if v >=2 :
        n_overlap += 1

print(n_overlap)

# Part 2
ocean_floor = defaultdict(int)
for l in lines:
    coordinates = l.strip().split('->')
    start = [int(p) for p in coordinates[0].split(',')]
    end = [int(p) for p in coordinates[1].split(',')]
    
    vent = generate_vent_diagonals(start, end)
    # print(vent)
    for p in vent:
        ocean_floor[p] += 1

n_overlap = 0
for _, v in ocean_floor.items():
    if v >=2 :
        n_overlap += 1

print(n_overlap)






