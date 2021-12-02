test = False

if test:
    input = '../inputs/day2_test'
else:
    input = '../inputs/day2_input'

# Part 1 
horizontal_dict = {'forward':1}
vertical_dict = {'up':-1, 'down':1}

vloc = 0
hloc = 0

with open(input, 'r') as f:
    lines = f.readlines()
lines = [l.strip().split() for l in lines]

for l in lines:
    dir, mag = l
    if dir in horizontal_dict:
        hloc += horizontal_dict[dir]*int(mag)
    else:
        vloc += vertical_dict[dir]*int(mag)

print(hloc*vloc)

# Part 2
horizontal_dict = {'forward':1}
vertical_dict = {'up':-1, 'down':1}

vloc = 0
hloc = 0
aim = 0 

with open(input, 'r') as f:
    lines = f.readlines()
lines = [l.strip().split() for l in lines]

for l in lines:
    dir, mag = l
    if dir in horizontal_dict:
        hloc += horizontal_dict[dir]*int(mag)
        vloc += aim*int(mag)
    else:
        aim += vertical_dict[dir]*int(mag)

print(hloc*vloc)