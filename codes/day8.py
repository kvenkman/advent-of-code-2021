from collections import defaultdict

test = False
if test:
    input = '../inputs/day8_test'
else:
    input = '../inputs/day8_input'

with open(input, 'r') as f:
    lines = f.readlines()

# Part 1
count = 0
for l in lines:
    output_words = l.strip().split("|")[1].strip().split()
    for w in output_words:
        if len(w) in [2, 3, 4, 7]:
            count += 1

print(count)

# Part 2
def decode_numbers(input_string):
    input_dict = defaultdict(list)
    segment_dict = {}

    for w in input_string.split():
        if len(w) == 2:
            segment_dict[1] = list(w)
        if len(w) == 3:
            segment_dict[7] = list(w)
        if len(w) == 4:
            segment_dict[4] = list(w)
        if len(w) == 7:
            segment_dict[8] = list(w) 

        input_dict[len(w)].append(w)
    
    # to find the combination for 6, add segments to segments(1) to obtain segments(8)
    s = input_dict[2][0]
    for w in input_dict[6]:
        if set(s+w) == set(input_dict[7][0]):
            break
    segment_dict[6] = list(w)
    input_dict[6].remove(w)

    # to find the combination for 0
    s = input_dict[4][0]
    for w in input_dict[6]:
        if set(s+w) == set(input_dict[7][0]):
            break
    segment_dict[0] = list(w)
    input_dict[6].remove(w)

    # the remaining 6 segment number must by 9
    w = input_dict[6][0]
    segment_dict[9] = list(w)

    # to find the combination for 2
    s = w # w currently corresponds to 9
    for w in input_dict[5]:
        if set(s+w) == set(input_dict[7][0]):
            break
    input_dict[5].remove(w)
    segment_dict[2] = list(w)

    # 5 + 1 produces 9
    # Remaining will be 3
    s1 = input_dict[2][0]
    s2 = s # s is still 9
    for w in input_dict[5]:
        if set(s1+w) == set(s2):
            break
    input_dict[5].remove(w)
    segment_dict[5] = list(w)

    # Remaining one should be 3
    w = input_dict[5][0]
    segment_dict[3] = list(w)

    return segment_dict

display_numbers = []
for l in lines:
    input_letters, output_words = l.strip().split("|")
    segment_dict = decode_numbers(input_letters.strip())

    numstr = ''
    for w in output_words.strip().split():
        for i in range(10):
            if set(segment_dict[i]) == set(w):
                break
        
        numstr += str(i)
    display_numbers.append(int(numstr))

print(sum(display_numbers))
