import random


class NumberGuessingGame:

    def __init__(self, min_number=1, max_number=100):
        self.min_number = min_number
        self.max_number = max_number
        self.reset_game()

    def reset_game(self):
        """Start a new game."""
        self.secret_number = random.randint(
            self.min_number,
            self.max_number
        )
        self.attempts = 0
        self.game_over = False

    def make_guess(self, guess):
        """Check the user's guess."""

        if self.game_over:
            return "Game Over"

        self.attempts += 1

        if guess < self.secret_number:
            return "Too Low"

        elif guess > self.secret_number:
            return "Too High"

        else:
            self.game_over = True
            return "Correct"

    def get_attempts(self):
        """Return the number of attempts."""
        return self.attempts