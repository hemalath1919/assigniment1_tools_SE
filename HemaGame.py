import random
import math
import sys


class HemaGame:
    WIN_COUNT_TOTAL = 5
    avail_options = ["rock", "paper", "scissors"]

    def __init__(self):
        self.totalPlayerWins = 0
        self.totalComputerWins = 0

    def input_from_computer_and_player(self):

        while True:
            userIn = input(
                "Enter from these options : rock, paper or scissors. Press (q) to quit the game or Press (r) for restart the game \n"
            )
            userIn = userIn.lower()
            if userIn == "r":
                self.main()

            if userIn == "q":
                sys.exit()

            if userIn not in self.avail_options:
                print("wrong option")
                continue
            else:
                break

        computer = self.computerSelection()

        if userIn == computer:
            return (0, userIn, computer)

        if self.isWin(userIn, computer):
            return (1, userIn, computer)

        return (-1, userIn, computer)

    def computerSelection(self):
        return random.choice(self.avail_options)

    def isWin(self, playerIn, computerIn):
        # return true is the player beats the computer
        # winning conditions: r > s, s > p, p > r
        if (
            (playerIn == "rock" and computerIn == "scissors")
            or (playerIn == "scissors" and computerIn == "paper")
            or (playerIn == "p" and computerIn == "r")
        ):
            return True
        return False

    def play_game(self):

        self.totalPlayerWins = 0
        self.totalComputerWins = 0

        while self.totalPlayerWins < self.WIN_COUNT_TOTAL and self.totalComputerWins < self.WIN_COUNT_TOTAL:
            result, user, computer = self.input_from_computer_and_player()
            # tie
            if result == 0:
                print(
                    "Draw. Player and the computer have both chosen {}. \n".format(
                        user
                    )
                )
            # player win
            elif result == 1:
                self.totalPlayerWins += 1
                print(
                    "Player chose {} and the computer chose {}. You won {} times \n".format(
                        user, computer, self.totalPlayerWins
                    )
                )
            else:
                self.totalComputerWins += 1
                print(
                    "Player chose {} and the computer chose {}. You lost sorry.. The computer won {}\n".format(
                        user, computer, self.totalComputerWins
                    )
                )

        if self.totalPlayerWins > self.totalComputerWins:
            print(
                "Player won 5 times and is the winner!! Congratulations :D"
            )
        else:
            print(
                "computer has won the game total 5 times!!"
            )

    def main(self):
        print("Restarting the game")
        self.play_game()


if __name__ == "__main__":
    game = HemaGame()
    game.play_game()
