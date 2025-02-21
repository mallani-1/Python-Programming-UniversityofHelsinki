This directory contains my solution for Exercise 1 of the exam

## 🔍 Task Overview

The task was to develop a program that achieves the following:

1. **Input Gathering**:
   - Continuously prompt the user to enter strings, concatenating them into a single string.
   - End input collection when the user enters an empty string (press Enter without typing).

2. **Frequency Calculation**:
   - Implement a `counter` function to return a dictionary with each character as keys and their respective counts as values.

3. **Filter by Frequency**:
   - Ask the user for a minimum frequency threshold `n`. Only characters appearing `n` times or more are displayed.

4. **Output**:
   - Present characters in order of their frequency, from most to least frequent.
   - Display each character's frequency as: `Character "X" was entered Y times`.

## 📄 Example Interaction:

```plaintext
Enter a string: hello
Enter a string: world
Enter a string: 
Minimum number of characters: 2
Characters in order of occurrence:
Character "l" was entered 3 times
Character "o" was entered 2 times