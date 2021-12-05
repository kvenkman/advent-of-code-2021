test = False

def return_rows(bingo_card, nrows = 5, ncols = 5):
    rows = []
    for i in range(nrows):
        rows.append(sum(bingo_card[i*ncols:(i+1)*ncols]))
    return rows
    
def return_cols(bingo_card, nrows = 5, ncols = 5):
    cols = []
    for i in range(ncols):
        cols.append(sum([bingo_card[j*ncols + i] for j in range(nrows)]))
    return cols

def calculate_score(bingo_card, draw):
    numbers = [i for i in bingo_card if i != -1]
    return(sum(numbers)*draw)

if test:
    input = '../inputs/day4_test'
else:
    input = '../inputs/day4_input'

with open(input, 'r') as f:
    lines = f.readlines()
    lines += ['']

draw_numbers = [int(number) for number in lines[0].strip().split(',')]
bingo_cards = []

new_card = ''
for l in lines[2:]:
    if l.strip() != '':
        new_card += l + ' '
    else:
        bingo_cards.append([int(entry) for entry in new_card.split()])
        new_card = ''

# Part 1
bingo_cards_copy = bingo_cards.copy()
win_flag = 0

for draw in draw_numbers:
    for card in bingo_cards_copy:
        while draw in card:
            card[card.index(draw)] = -1
        
        rows, cols = return_rows(card), return_cols(card)
        if -5 in rows or -5 in cols:
            print(calculate_score(card, draw))
            win_flag = 1
            break
    if win_flag:
        break

# Part 2
winning_scores = []
win_flag = 0
bingo_cards_copy = bingo_cards.copy()
winning_cards = []

for draw in draw_numbers:
    for card in bingo_cards_copy:
        while draw in card:
            card[card.index(draw)] = -1
        
        rows, cols = return_rows(card), return_cols(card)
        if -5 in rows or -5 in cols:
            winning_scores.append(calculate_score(card, draw))
            winning_cards.append(card)


    if winning_cards:
        bingo_cards_copy = [b for b in bingo_cards_copy if b not in winning_cards]
        winning_cards = []


print(winning_scores[-1])



