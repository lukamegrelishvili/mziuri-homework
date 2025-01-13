import random

def create_words_file():
    words = ["PYTHON", "HANGMAN", "COMPUTER", "PROGRAMMING", "DEVELOPER", "SOFTWARE", "DEBUG"]
    try:
        with open('words.txt', 'w') as file:
            file.write('\n'.join(words))
        print("words.txt file created successfully.")
    except Exception as e:
        print(f"Error creating words.txt: {e}")

def select_word():
    try:
        with open('words.txt', 'r') as file:
            words = file.read().splitlines()
        return random.choice(words)
    except FileNotFoundError:
        print("Error: words.txt file not found.")
        return None

def display_word(word, guessed_letters):
    return ''.join([letter if letter in guessed_letters else '_' for letter in word])

def get_user_guess(guessed_letters):
    while True:
        guess = input("Enter a letter: ").upper()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
        elif guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
        else:
            return guess

def update_game_state(word, guessed_letters, remaining_attempts, guess):
    if guess in word:
        guessed_letters.add(guess)
        print(f"Good guess! {guess} is in the word.")
    else:
        remaining_attempts -= 1
        print(f"Sorry, {guess} is not in the word. {remaining_attempts} attempts left.")
    return remaining_attempts

def check_win(word, guessed_letters):
    return set(word).issubset(guessed_letters)

def check_game_over(remaining_attempts, word, guessed_letters):
    if remaining_attempts <= 0:
        print(f"Game over! The word was: {word}")
        return True
    if check_win(word, guessed_letters):
        print(f"Congratulations! You've guessed the word: {word}")
        return True
    return False

def main():
    create_words_file()
    print("Welcome to Hangman!")

    while True:
        word = select_word()
        if not word:
            break

        guessed_letters = set()
        remaining_attempts = 6

        while True:
            print("\nWord: ", display_word(word, guessed_letters))
            print("Guessed letters: ", ' '.join(sorted(guessed_letters)))

            guess = get_user_guess(guessed_letters)
            remaining_attempts = update_game_state(word, guessed_letters, remaining_attempts, guess)

            if check_game_over(remaining_attempts, word, guessed_letters):
                break

        play_again = input("Do you want to play again? (y/n): ").lower()
        while play_again not in ['y', 'n']:
            play_again = input("Invalid input. Do you want to play again? (y/n): ").lower()
        if play_again == 'n':
            print("Thanks for playing Hangman! Goodbye!")
            break

if __name__ == "__main__":
    main()
