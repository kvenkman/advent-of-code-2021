from collections import defaultdict

test = False

if test:
    input = '../inputs/day14_test'
else:
    input = '../inputs/day14_input'

with open(input, 'r') as f:
    lines = f.readlines()

polymer_template = lines[0].strip()
insertion_rules = {}

for l in lines[2:]:
    one, two = l.strip().split(' -> ')
    insertion_rules[one] = two

# Part 1
for _ in range(10):
    new_template = ''
    for i, _ in enumerate(polymer_template[:-1]):
        s = polymer_template[i:i+2]
        v = insertion_rules[s]
        new_template += s[0] + v
    new_template += s[-1]
    polymer_template = new_template

count = defaultdict(int)
for c in polymer_template:
    count[c] += 1

min_count, max_count = None, None
for k, v in count.items():
    if not min_count:
        min_count = count[k]
    else:
        min_count = count[k] if count[k] < min_count else min_count
    
    if not max_count:
        max_count = count[k]
    else:
        max_count = count[k] if count[k] > max_count else max_count

print(max_count - min_count)

# Part 2
# Need to rethink the way polymerization is done

polymer_template = lines[0].strip()
polymer_dict = defaultdict(int)

# initial parse
for i, _ in enumerate(polymer_template[:-1]):
    s = polymer_template[i:i+2]
    polymer_dict[s] += 1

# Now to create the polymer
for i in range(40):
    new_poly_dict = defaultdict(int)
    for k in polymer_dict.keys():
        s1 = k[0] + insertion_rules[k]
        s2 = insertion_rules[k] + k[1]

        new_poly_dict[s1] += polymer_dict[k]
        new_poly_dict[s2] += polymer_dict[k]
    polymer_dict = new_poly_dict

count = defaultdict(int)
for k in polymer_dict.keys():
    count[k[0]] += polymer_dict[k]
    # count[k[1]] += polymer_dict[k]

count[polymer_template[-1]] += 1

min_count, max_count = None, None
for k, v in count.items():
    if not min_count:
        min_count = count[k]
    else:
        min_count = count[k] if count[k] < min_count else min_count
    
    if not max_count:
        max_count = count[k]
    else:
        max_count = count[k] if count[k] > max_count else max_count

print(max_count - min_count)