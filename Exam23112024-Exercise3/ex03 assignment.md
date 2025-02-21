# 🎲 Lottery Simulator

This directory contains my solution for Exercise 3 of the exam, implemented in Python to simulate a lottery draw and calculate potential winnings based on ticket entries.

## 🔍 Task Overview

The task was to create a program that simulates a lottery system with the following components:

1. **Lottery Draw**:
   - Implement a `draw_numbers` function to randomly select and return 7 unique numbers from 1 to 39.

2. **Calculate Winnings**:
   - Implement a `calculate_winnings` function that takes a list of hit counts for each ticket entry and calculates the total winnings based on specified prize tiers for each line:
     - 4 correct numbers: €10
     - 5 correct numbers: €50
     - 6 correct numbers: €2,750
     - 7 correct numbers: €6,500,000

3. **Play Lottery**:
   - Implement a `play_lottery` function that checks each line of the player's ticket (a list of lists of numbers) against the winning numbers.
   - Calculate the number of correct hits per line and sum up the winnings for all lines.
   - Return a message indicating the total amount won, if any.

## 📄 Example Interaction:

```python
# Example tickets
ticket = [
    [2, 3, 7, 10, 15, 23, 35],
    [1, 5, 9, 14, 18, 22, 30],
    [4, 8, 12, 16, 20, 24, 28]
]

# Running the lottery simulation
result = play_lottery(ticket)
print(result)  # Output could be "You won X euros!", where X is the sum of winnings from all lines.