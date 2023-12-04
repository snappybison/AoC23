# Read input text file

with open("day_4_input.txt") as file:
    lines = [line.rstrip() for line in file]

## -------------------------------------------- ##

# Get a list with the score of each card  

score_list = []

for line in lines:

    # Remove "Card #:" from every line and put numbers in a list and filter spaces and pipes
    numbers = line.split(':')[1].split(' ')
    total_numbers = [i for i in numbers if i != '' and i != '|']

    # Each duplicate in combined winning and card numbers means a winning number, then add to list of scores for each card
    score = len(total_numbers) - len(set(total_numbers))
    score_list.append(score)

## -------------------------------------------- ##

# Recursively inspect cards and add cards won to global variable

def read_card(card):

    global total_cards

    # Get how many winning numbers in this card and 
    points = score_list[card]
    total_cards += points

    # Starting from the next card and ending dependant on how many points, read the cards won from this card
    start = card + 1
    end = start + points

    for card in range(start, end):
        read_card(card)

## -------------------------------------------- ##

# Starting with one of each card
total_cards = len(lines)

for card in range(total_cards):
    read_card(card)

print(total_cards)
