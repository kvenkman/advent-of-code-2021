from collections import defaultdict

test = False

if test:
    input = '../inputs/day7_test'
else:
    input = '../inputs/day7_input'

with open(input, 'r') as f:
    lines = f.readlines()

hpos = defaultdict(int)
for k in lines[0].strip().split(','):
    hpos[int(k)] += 1

# Part 1
cost_dict = {}
min_cost, min_pos = None, None
for i in range(min(hpos.keys()), max(hpos.keys())+1):
    cost_dict[i] = sum([abs(i-j)*hpos[j] for j in hpos.keys()])
    if (min_cost == None) or (cost_dict[i] < min_cost):
        min_cost = cost_dict[i]
        min_pos = i
print(min_cost, min_pos)

# Part 2
def move_crab_cost(amount):
    return amount*(amount+1)/2

cost_dict = {}
min_cost, min_pos = None, None
for i in range(min(hpos.keys()), max(hpos.keys())+1):
    cost_dict[i] = sum([move_crab_cost(abs(i-j))*hpos[j] for j in hpos.keys()])
    if (min_cost == None) or (cost_dict[i] < min_cost):
        min_cost = cost_dict[i]
        min_pos = i
print(min_cost, min_pos)
