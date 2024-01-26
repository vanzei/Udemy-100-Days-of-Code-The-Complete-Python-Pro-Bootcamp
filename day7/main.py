# List of words

hangman_art = {6:
    """
     -----
         |
         |
         |
         |
         |
    """, 5:
    """
     -----
     O   |
         |
         |
         |
         |
    """, 4:
    """
     -----
     O   |
     |   |
         |
         |
         |
    """, 3:
    """
     -----
     O   |
    /|   |
         |
         |
         |
    """, 2:
    """
     -----
     O   |
    /|\\  |
         |
         |
         |
    """, 1:
    """
     -----
     O   |
    /|\\  |
    /    |
         |
         |
    """, 0:
    """
     -----
     O   |
    /|\\  |
    / \\  |
         |
         |
    """
}


words_list = ['apple',  'pineapple', 'lettuce', 'mouse']

# Select a random one

import random

word = random.choice(words_list)
printable = ['_'] * len(word)

## User to guess a letter
lifes = 6
while lifes > 0 and '_' in printable:
    print(hangman_art[lifes])
    print(''.join(printable))
    letter = input('Choose a letter \n\n').lower()
    if letter in word:
        for index, l in enumerate(word):
            if letter == l:
                printable[index] = letter
    else:
        print(f'The letter {letter} is not in this word \n')
        lifes -= 1
if lifes == 0:
    print(hangman_art[lifes])
    print('You lost!')
else:
    print(''.join(printable))
    print('You won!')   




        