import random


def play_number_guess(low: int = 1, high: int = 30, max_attempts: int = 7) -> None:
    secret = random.randint(low, high)
    attempts_left = max_attempts
    score = 100
    guesses = []

    print(f"Guess the secret number between {low} and {high}.")
    print(f"You have {max_attempts} attempts. Starting score: {score}\n")

    while attempts_left > 0:
        raw = input(f"Attempt {max_attempts - attempts_left + 1}/{max_attempts} - Enter guess: ").strip()

        try:
            guess = int(raw)
        except ValueError:
            print("Invalid input. Please enter a whole number.\n")
            continue

        if guess < low or guess > high:
            print(f"Out of range! Pick a number from {low} to {high}.\n")
            continue

        if guess in guesses:
            print(f"You already tried {guess}. Try a different number.\n")
            continue

        guesses.append(guess)
        attempts_left -= 1

        if guess == secret:
            print(f"\nCorrect! The secret number was {secret}.")
            print(f"Final score: {score} | Guesses used: {len(guesses)} -> {guesses}")
            return

        # Penalty scales with how close or far the guess is
        diff = abs(secret - guess)
        penalty = 10 if diff <= 3 else 20
        score = max(0, score - penalty)

        direction = "higher" if guess < secret else "lower"
        proximity = "very close" if diff <= 3 else ("getting closer" if diff <= 10 else "far")
        print(f"Go {direction} ({proximity}). Score: {score} | Attempts left: {attempts_left}\n")

    print(f"\nGame over! The secret number was {secret}.")
    print(f"Your guesses: {guesses} | Final score: {score}")


if __name__ == "__main__":
    play_number_guess()