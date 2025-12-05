import random

# -----------------------------
# 20 WORDS WITH CLUES
# -----------------------------
WORDS = [
    # Fruits – 5
    ("apple", "A red or green fruit that keeps doctors away"),
    ("banana", "A long yellow fruit"),
    ("mango", "King of fruits"),
    ("orange", "A citrus fruit and a color"),
    ("grapes", "Small fruits that come in bunches"),

    # Computer Hardware – 5
    ("keyboard", "Hardware used to type letters"),
    ("mouse", "You click it to control the computer"),
    ("monitor", "It displays output on the screen"),
    ("printer", "Hardware that gives a paper output"),
    ("processor", "The brain of the computer"),

    # Programming languages – 5
    ("python", "A popular language named after a comedy group"),
    ("java", "A language named after a type of coffee"),
    ("csharp", "Microsoft language written as C#"),
    ("javascript", "Language used for web interactivity"),
    ("ruby", "A language also the name of a red gemstone"),

    # Car brands – 5
    ("tata", "A famous Indian car brand"),
    ("bmw", "Luxury German brand with blue/white logo"),
    ("audi", "German brand with four rings"),
    ("tesla", "Electric car brand by Elon Musk"),
    ("ford", "American car company started by Henry Ford")
]

# -----------------------------
# MAIN GAME
# -----------------------------
def play_hangman():
    # Choose a random (word, clue)
    secret, clue = random.choice(WORDS)

    guessed = []
    wrong = 0
    max_wrong = 6

    print("\n🎯 Welcome to Hangman with Clues!")
    print("Clue:", clue)     # Show the clue here
    print(f"You have {max_wrong} wrong attempts.\n")

    while wrong < max_wrong:
        # Show progress
        display = ""
        for ch in secret:
            if ch in guessed:
                display += ch + " "
            else:
                display += "_ "
        print("Word:", display)
        print("Wrong attempts:", wrong, "/", max_wrong)

        guess = input("Enter a letter: ").lower()

        # Validation
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter only one alphabet letter.\n")
            continue

        if guess in guessed:
            print("You already guessed that.\n")
            continue

        guessed.append(guess)

        # Check guess
        if guess in secret:
            print("✔ Correct guess!\n")
        else:
            wrong += 1
            print("❌ Wrong guess!\n")

        # Check winning
        if all(ch in guessed for ch in secret):
            print("\n🎉 You won! The word was:", secret)
            return

    # Out of attempts
    print("\n💀 Game Over! The word was:", secret)


# -----------------------------
# START PROGRAM
# -----------------------------
if __name__ == "__main__":
    play_hangman()