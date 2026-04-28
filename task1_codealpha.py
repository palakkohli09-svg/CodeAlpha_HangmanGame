import random

words = ["apple", "tiger", "chair", "robot", "plant"]
word = random.choice(words)

guessed_word = ["_"] * len(word)
guessed_letters = []
wrong_guesses = 0
max_wrong = 6

print("welcome to Hangman!")

while wrong_guesses < max_wrong and "_" in guessed_word:
    print("\nWord:", " ".join(guessed_word))
    guess = input("enter a letter: ").lower()

    if guess in guessed_letters:
        print("you already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("correct!")
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess

    else:
        wrong_guesses += 1
        print(f"Wrong! Attempts left: {max_wrong - wrong_guesses}")

#final result
if "_" not in guessed_word:
    print("\n you won! The word was:", word)
else:
    print("\n you lost! the word was:", word)