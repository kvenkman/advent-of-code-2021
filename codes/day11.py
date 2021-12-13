from collections import deque
test = False

if test:
    input = '../inputs/day11_test'
else:
    input = '../inputs/day11_input'

with open(input, 'r') as f:
    lines = f.readlines()

octo_map = [[int(i) for i in list(x.strip())] for x in lines]

# Part 1
def return_adjacents(i, j, size):
    adjacents = []
    for x in range(-1, 2):
        for y in range(-1, 2):
            if i+x in size[0] and j+y in size[1]:
                adjacents.append((i+x, j+y))
    
    return adjacents

def update_cell_val(i, j, value, size):
    value += 1
    if value > 9:
        return 0, True, return_adjacents(i, j, size)
    else:
        return value, False, []

def step(o_map):
    n_flashes = 0
    current_flashed = set()
    adjacents = deque()
    size = (list(range(len(o_map))), list(range(len(o_map[0]))))

    for i, row in enumerate(o_map):
        for j, _ in enumerate(row):
            o_map[i][j], flashed, new_adjacents = update_cell_val(i, j, o_map[i][j], size)
            if flashed:
                current_flashed.add((i, j))
            for item in new_adjacents:
                adjacents.append(item)
    
    while adjacents:
        item = adjacents.popleft()
        if item not in current_flashed:
            i, j = item
            o_map[i][j], flashed, new_adjacents = update_cell_val(i, j, o_map[i][j], size)
            if flashed:
                current_flashed.add(item)
            for x in new_adjacents:
                adjacents.append(x)
    
    return o_map, len(current_flashed), len(current_flashed) ==  len(o_map)*len(o_map[0])


steps = 100
flash_count = 0

for i in range(steps):
    octo_map, n_flashes, _ = step(octo_map)
    flash_count += n_flashes

print(flash_count)

# Part 2
octo_map = [[int(i) for i in list(x.strip())] for x in lines] # Re-read inputs
n_steps = 0
while True:
    octo_map, n_flashes, sync = step(octo_map)
    n_steps += 1
    if sync:
        break

print(n_steps)