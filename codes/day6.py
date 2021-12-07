from collections import defaultdict

test = False
if test:
    input = '../inputs/day6_test'
else:
    input = '../inputs/day6_input'

with open(input, 'r') as f:
    lines = f.readlines()

fishes = [int(d) for d in lines[0].strip().split(',')]

# Part 1
for _ in range(80):
    count_new_fishies = 0
    for i, d in enumerate(fishes):
        if d == 0:
            fishes[i] = 6
            count_new_fishies += 1
        else:
            fishes[i] -= 1
    for i in range(count_new_fishies):
        fishes.append(8)

print(len(fishes))

# Part 2
fishes = defaultdict(int)
initial_count = [int(d) for d in lines[0].strip().split(',')]

for i in initial_count:
    fishes[i] += 1

for i in range(256):
    new_dict = defaultdict(int)
    for k in sorted(fishes.keys()):
        if k == 0:
            new_dict[6] = fishes[0]
            new_dict[8] = fishes[0]
        else:
            new_dict[k-1] += fishes[k]
    fishes = new_dict

fish_count = 0
for k, v in fishes.items():
    fish_count += v

print(fish_count)