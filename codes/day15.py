from collections import defaultdict

test = False

if test:
    input = '../inputs/day15_test'
else:
    input = '../inputs/day15_input'

with open(input, 'r') as f:
    lines = f.readlines()

cave_map = [[int(x) for x in list(l.strip())] for l in lines]
cave_map[0][0] = 0

# Part 1
c_lim = len(cave_map[0]) - 1
r_lim = len(cave_map) - 1

# cost_map = defaultdict(int)
cost_map = {}
cost_map[(c_lim, r_lim)] = cave_map[r_lim][c_lim]

def check_valid(c_pos, r_pos):
    if c_pos<0 or c_pos>=len(cave_map[0]) or r_pos<0 or r_pos >= len(cave_map):
        return False
    else:
        return True

def check_around(col, row):
    for p in [(col-1, row), (col, row-1), (col, row+1), (col, row+1)]:
        if check_valid(*p) and (p in cost_map):
            if cost_map[p] < cost_map[(col, row)]:
                cost_map[(col, row)] = cave_map[row][col] + cost_map[p]

def calc_cost_map(col, row, prev=None):
    if (col, row) in cost_map:
        return cost_map[(col, row)]

    adj_costs = set()

    for p in [(col, row+1), (col+1, row)]:
        if p == prev:
            continue
        if check_valid(*p):
            if p in cost_map:
                adj_costs.add(cost_map[p])
            else:
                adj_costs.add(calc_cost_map(*p, (col, row)))
    
    cost_map[(col, row)] = cave_map[row][col] + min(adj_costs)

    return cost_map[(col, row)]

print(calc_cost_map(0, 0))
print(c_lim, r_lim, len(cost_map))