def reverse_word(s, start, end):
    while start < end:
        # Swap characters at start and end indices
        s[start], s[end] = s[end], s[start]
        # Move start index forward
        start = start + 1
        # Move end index backward
        end -= 1

s = input()  # Take input from the user
s = list(s)  # Convert input string to a list of characters
start = 0  # Start index for word reversal

while True:
    try:
        # Find the index of the next space character (' ') starting from 'start'
        end = s.index(' ', start)
        # Reverse the word between 'start' and 'end - 1'
        reverse_word(s, start, end - 1)
        # Move 'start' index to the next word
        start = end + 1

    except ValueError:  # If no more spaces are found, reverse the last word
        # Reverse the last word from 'start' to the end of the list
        reverse_word(s, start, len(s) - 1)
        break

s.reverse()  # Reverse the entire list of characters
s = "".join(s)  # Convert the list of characters back to a string
print(s)  # Print the final reversed string
