import random
HANGMAN = (
    """
    ------
    |    |
    |
    |
    |
    |
    |
    |
    |
    --------
    """,
    """
    ------
    |    |
    |    O  |
    |
    |
    |
    |
    |
    |
    --------
    """,
    """
    ------
    |    |
    |    O
    |   -+-
    |
    |
    |
    |
    |
    --------
    """,
    """
    ------
    |    |
    |    O
    |  /-+-/
    |
    |
    |
    |
    |
    --------
    """,
    """
    ------
    |    |
    |    O
    |  /-+-/
    |    |
    |
    |
    |
    |
    --------
    """,
    """
    ------
    |    |
    |    O
    |  /-+-/
    |    |
    |    |
    |   |
    |   |
    |
    --------
    """,
    """
    ------
    |    |
    |    O
    |  /-+-/
    |    |
    |    |
    |   | |
    |   | |
    |
    --------
    """
)
MAX_WRONG = len(HANGMAN) - 1
WORDS = ("MZIURI", "PROGRAMMING", "SCHOOL", "SKIBIDI", "PYTHON", "RIZZ", "MONEY")
word = random.choice(WORDS) #sityva romelic unda amoicnos
so_far = "-" * len(word)#yovel asos naxulobs
wrong = 0 #dashvebuli shecdomebis raodenoba
used = []#amocnobili asoebis raodenoba
# main cikli
print("WELCOME TO HANGMAN GAME! :D")
print(
    """
    Now I will think of a word, and you will have to guess it letter by letter.
You will suggest one letter at a time, and if this letter is in my word, I will reveal its position in the word.
If it’s not, I will start drawing a stick figure on the gallows.
The game will continue until you guess the word or the stick figure is fully hanged.
So, good luck! The fate of the poor little stick figure depends on you!
    """
)
while wrong < MAX_WRONG and so_far != word:
    print(HANGMAN[wrong])
    print("\nYou have already suggested the following letters::\n", used)
    print("\nThe word you’ve guessed so far looks like this:\n", so_far)
    # momxmareblis inputi
    guess = input("\n\ntype letter: ")
    guess = guess.upper()
    while guess in used:
        print("u already guessed this letter: ", guess)
        guess = input("\ntype letter: ")
        guess = guess.upper()
    used.append(guess)
    # naxulobs aris tu ara es aso sityvashi
    if guess in word:
        print("\nYE! the letter", guess, "is in word!!")
        new = ""
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += so_far[i]
        so_far = new
    else:
        print("\nunfortunately ", guess, "is not in word.")
        wrong += 1
# tamashis dasasruli
if wrong == MAX_WRONG:
    print(HANGMAN[wrong])
    print("\nthey hanged the man!")
else:
    print("\nu guessed!")
print("\nthe word was", word, ".")
input("\n\nPress ENTER to EXIT.")
