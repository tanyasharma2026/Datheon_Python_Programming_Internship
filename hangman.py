import random

HANGMAN_STAGES = [
    """
       +---+

       |   |
           |
           |
           |
           |
    =========
    """,
    """
       +---+

       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       +---+

       |   |
       O   |

       |   |
           |
           |
    =========
    """,
    """
       +---+

       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       +---+

       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
    """
       +---+

       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,
    """
       +---+

       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """
]

WORDS_LIST = ["PYTHON", "DATHEON", "ENGINEERING", "PROGRAMMING", "CHATBOT", "DEVELOPER"]

def play_hangman():
    secret_word = random.choice(WORDS_LIST).upper()
    guessed_letters = set()
    wrong_attempts = 0
    max_attempts = 6

    print("=======================================")
    print("Welcome to the Terminal Hangman Game!")
    print("=======================================")

    while wrong_attempts < max_attempts:
        print(HANGMAN_STAGES[wrong_attempts])
        
        display_word = [letter if letter in guessed_letters else "_" for letter in secret_word]
        print("Word to guess: " + " ".join(display_word))
        print(f"Attempts remaining: {max_attempts - wrong_attempts}")
        print(f"Guessed letters: {', '.join(sorted(list(guessed_letters)))}")
        print("---------------------------------------")

        if "_" not in display_word:
            print(f"🎉 CONGRATULATIONS! You won! The word was: {secret_word}")
            break

        guess = input("Guess a letter: ").strip().upper()

        if len(guess) != 1 or not guess.isalpha():
            print("❌ Invalid input! Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print(f"⚠️ You already guessed the letter '{guess}'. Try another one!")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            print(f"✅ Good job! '{guess}' is in the word.")
        else:
            print(f"❌ Oops! '{guess}' is not in the word.")
            wrong_attempts += 1

    if wrong_attempts == max_attempts:
        print(HANGMAN_STAGES[wrong_attempts])
        print("💥 GAME OVER! You ran out of attempts.")
        print(f"The secret word was: {secret_word}")

if __name__ == "__main__":
    play_hangman()
  
