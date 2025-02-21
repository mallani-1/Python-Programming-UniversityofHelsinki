# Write your solution to exercise 3 here
from random import sample

def draw_numbers():
    list1 = list(range(1,40))
    list2 = sorted(sample(list1,7))   
    return list2

def calculate_winnings(hits: list):
    s = 0
    for i in hits:
        if i == 4:
            s = s + 10
        elif i == 5:
            s = s + 50
        elif i == 6:
            s = s + 2750
        elif i == 7:
            s = s + 6500000
    return s
        
def play_lottery(ticket: list):
    win = draw_numbers()
    hits = []
    for i in ticket:
        s = 0
        for j in i:
            s = s + win.count(j)
        hits.append(s)
    winnings = calculate_winnings(hits)
    if winnings > 0:
        return f"You won {winnings} euros!"
    else:
        return "No winnings!"