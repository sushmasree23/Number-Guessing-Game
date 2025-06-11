import random

MIN, MAX = 1, 100
MAX_ATTEMPTS = 10

def play():
    secret = random.randint(MIN, MAX)
    attempts_left = MAX_ATTEMPTS
    print(f"🔢  I'm thinking of a number between {MIN} and {MAX}.")
    print(f"💡  You have {MAX_ATTEMPTS} attempts. Good luck!\n")

    while attempts_left:
        try:
            guess = int(input(f"Attempt {MAX_ATTEMPTS - attempts_left + 1}: Enter your guess ► "))
        except ValueError:
            print("⛔  Please enter a valid integer.\n")
            continue

        attempts_left -= 1

        if guess == secret:
            print(f"\n🎉  Correct! {guess} is the number. You won in {MAX_ATTEMPTS - attempts_left} attempts.")
            break
        elif guess < secret:
            print("📈  Too low!\n")
        else:
            print("📉  Too high!\n")

        if attempts_left == 0:
            print(f"💥  Out of attempts! The number was {secret}.")

    print("\nThanks for playing!")

if __name__ == "__main__":
    play()
