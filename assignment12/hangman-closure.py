#4
def make_hangman(secret_word):
    guesses = []

    def hangman_closure(letter):
        guesses.append(letter)
        display = ''
        all_guessed = True

        for char in secret_word:
            if char in guesses:
                display += char
            else:
                display += '_'
                all_guessed = False

        print(display)
        return all_guessed

    return hangman_closure


def main():
    secret_word = input("Enter the secret word: ").lower()
    print("\n" * 50)  # Clear the screen
    print("Let's play Hangman!\n")

    guess_fn = make_hangman(secret_word)

    while True:
        letter = input("Enter your guess (a single letter): ").lower()
        if len(letter) != 1 or not letter.isalpha():
            print("Please enter a single alphabetical character.")
            continue

        if guess_fn(letter):
            print("Congratulations! You guessed the word!")
            break


if __name__ == "__main__":
    main()