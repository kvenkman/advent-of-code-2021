test = False

if test:
    input_file = '../inputs/day1_test'
else:
    input_file = '../inputs/day1_input'

with open(input_file, 'r') as f:
    lines = f.readlines()

lines = [int(l.strip()) for l in lines]

# Part 1 
count = 0
for i, l in enumerate(lines):
    if i == 0:
        continue

    if l > lines[i-1]:
        count += 1

print(count)

# Part 2
count = 0
window_sums = []

for i, l in enumerate(lines):
    if (i == 0) or (i == len(lines)-1):
        continue

    window_sums.append(l + lines[i-1] + lines[i+1])

#print(window_sums)

for i, l in enumerate(window_sums):
    if i == 0:
        continue

    if l > window_sums[i-1]:
        count += 1

print(count)


