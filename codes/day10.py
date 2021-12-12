test = False

if test:
    input = '../inputs/day10_test'
else:
    input = '../inputs/day10_input'

with open(input, 'r') as f:
    lines = f.readlines()

cscore_dict = {')':3, ']':57, '}':1197, '>':25137}
bracket_dict = {')':'(', ']':'[', '}':'{', '>':'<'}

def complete_line(line):
    score_table  = {'(':1, '[':2, '{':3, '<':4}
    score = 0
    chunk = ''
    for c in list(line):
        if c not in bracket_dict:
            chunk += c
        else:
            if chunk[-1] == bracket_dict[c]:
                chunk = chunk[:-1]
    
    for c in list(chunk[::-1]):
        score = score*5 + score_table[c]

    return score

def check_corrupted(line):
    chunk = ''
    corrupt_flag = 0
    for c in list(line):
        if c not in bracket_dict:
            chunk += c
        else:
            if chunk[-1] == bracket_dict[c]:
                chunk = chunk[:-1]
            else:
                corrupt_flag = 1
                break
    
    if corrupt_flag != 0:
        return c
    else: 
        return None

# Part 1
syntax_error_score = 0
incomplete_lines = []

for l in lines:
    c = check_corrupted(l.strip())
    if c:
        syntax_error_score += cscore_dict[c]
    else:
        incomplete_lines.append(l.strip())

print(syntax_error_score)

# Part 2
syntax_error_score = []
for l in incomplete_lines:
    syntax_error_score.append(complete_line(l))

syntax_error_score.sort()

print(syntax_error_score[round(len(syntax_error_score)/2)-1])