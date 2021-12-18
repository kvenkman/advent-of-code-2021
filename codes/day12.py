from collections import defaultdict, deque
test = False

if test:
    input = '../inputs/day12_test'
else:
    input = '../inputs/day12_input'

with open(input, 'r') as f:
    lines = deque(f.readlines())

# Bit of skulduggery because there are multiple test cases provided
input_cases = []
new_entry = []
while lines:
    l = lines.popleft().strip()
    if l != '':
        new_entry.append(l)
    else:
        input_cases.append(new_entry)
        new_entry = []

def build_map(raw_inputs):
    for l in raw_inputs:
        one, two = l.split('-')

        if one not in ['start', 'end'] and two not in ['start', 'end']:
            cave_map[one].add(two)
            cave_map[two].add(one)
        else:
            if one == 'start' or two == 'end':
                cave_map[one].add(two)
            if one == 'end' or two == 'start':
                cave_map[two].add(one)
    
    return cave_map

# Part 1
def find_paths(starting_point, current_path, cave_map):
    found_paths = []

    for v in cave_map[starting_point]:
        if v.islower() and (v in current_path):
            # found_paths.append([v])
            continue
        found_paths += find_paths(v, current_path+[starting_point], cave_map)

    if not found_paths:
        found_paths = [[starting_point]]
    else:
        found_paths = [[starting_point] + x for x in found_paths]

    return found_paths

for i, case in enumerate(input_cases):
    cave_map = defaultdict(set)
    cave_map = build_map(case)
    paths = find_paths('start', ['start'], cave_map)
    n_paths = 0
    for p in paths:
        if ('start' in p) and ('end' in p):
            n_paths += 1
            
    print(n_paths)

# Part 2
print("******")
def find_paths_p2(starting_point, current_path, cave_map):
    found_paths = []

    for v in cave_map[starting_point]:
        flag = []
        if v.islower() and (v in current_path):
            # check if small cave is already in current_path
            loc = current_path.index(v)
            if v not in current_path[loc+1:] and -1 not in current_path:
                # check if there's a second occurrence. if not, insert a flag to indicate a small cave has been visited twice
                flag = [-1]
            else:
                continue
        found_paths += find_paths_p2(v, current_path+flag+[starting_point], cave_map)

    if not found_paths:
        found_paths = [[starting_point]]
    else:
        found_paths = [[starting_point] + x for x in found_paths]

    return found_paths

for i, case in enumerate(input_cases):
    cave_map = defaultdict(set)
    cave_map = build_map(case)
    paths = find_paths_p2('start', ['start'], cave_map)
    n_paths = 0
    for p in paths:
        if ('start' in p) and ('end' in p):
            n_paths += 1
            
    print(n_paths)