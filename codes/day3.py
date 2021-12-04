def most_common_bit(numbers, location):
    numsum = sum([1 for d in numbers if d[location] == '1'])
    return 1 if numsum >= len(numbers)/2 else 0

def least_common_bit(numbers, location):
    return 1-most_common_bit(numbers, location)

test = False

if test:
    input = '../inputs/day3_test'
else:
    input = '../inputs/day3_input'

with open(input, 'r') as f:
    lines = f.readlines()
    lines = [l.strip() for l in lines]

# Part 1
sums = [0]*len(lines[0])
for l in lines:
    for i, digit in enumerate(list(l)):
        sums[i] += int(digit)

gamma_rate = ''.join([str(round(digit/len(lines))) for digit in sums])
epsilon_rate = ''.join([str(1-round(digit/len(lines))) for digit in sums])

print(int(gamma_rate, 2)*int(epsilon_rate, 2))

# Part 2
# find oxygen generator rating
lcopy = lines.copy()
idx = 0
while (len(lcopy) > 1):
    digit = str(most_common_bit(lcopy, idx))
    lcopy = [l for l in lcopy if l[idx] == digit]
    idx += 1

ogr = lcopy[0]

# find CO2 scrubber rating
lcopy = lines.copy()
idx = 0
while (len(lcopy) > 1):
    digit = str(least_common_bit(lcopy, idx))
    lcopy = [l for l in lcopy if l[idx] == digit]
    idx += 1

csr = lcopy[0]

print(int(ogr, 2)*int(csr, 2))