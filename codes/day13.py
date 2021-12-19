test = False

if test:
    input = '../inputs/day13_test'
else:
    input = '../inputs/day13_input'

with open(input, 'r') as f:
    lines = f.readlines()

coordinates = set()
for i, l in enumerate(lines):
    if not l.strip():
        break
    x, y = int(l.strip().split(',')[0]), int(l.strip().split(',')[1])
    coordinates.add((x, y))

folds = lines[i+1:]
folds = [l.strip().split('fold along ')[1] for l in folds]

fold_vals = []
for f in folds:
    loc = int(f.split('=')[1])
    if 'x' in f:
        fold_vals.append([loc, 0])
    else:
        fold_vals.append([0, loc])

def y_fold(coordinates, y_fold):
    new_coordinates = set()

    for x, y in coordinates:
        if y > y_fold:
            new_coordinates.add((x, 2*y_fold-y))
        else:
            new_coordinates.add((x, y))
    return new_coordinates

def x_fold(coordinates, x_fold):
    new_coordinates = set()

    for x, y in coordinates:
        if x > x_fold:
            new_coordinates.add((2*x_fold-x, y))
        else:
            new_coordinates.add((x, y))
    return new_coordinates

# Part 1
x0, y0 = fold_vals[0]
if x0:
    new_coordinates = x_fold(coordinates, x0)
else:
    new_coordinates = y_fold(coordinates, y0)

print(len(new_coordinates))

# Part 2
coordinates = set()
for i, l in enumerate(lines):
    if not l.strip():
        break
    x, y = int(l.strip().split(',')[0]), int(l.strip().split(',')[1])
    coordinates.add((x, y))

for v in fold_vals:
    x0, y0 = v
    if x0:
        new_coordinates = x_fold(coordinates, x0)
    else:
        new_coordinates = y_fold(coordinates, y0)

    coordinates = new_coordinates

max_x, max_y = 0, 0
for x, y in new_coordinates:
    if x > max_x:
        max_x = x
    if y > max_y:
        max_y = y
    
for i in range(max_x+1):
    current_line = ''
    for j in range(max_y+1):
        if (i, max_y-j) in new_coordinates:
            current_line += '#'
        else:
            current_line += '.'
    print(current_line)
