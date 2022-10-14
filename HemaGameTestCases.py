import unittest
from HemaGame import HemaGame


class UnitTestRPSGame(unittest.TestCase):


    def test_computerRandomlyPicksOptions(self):
        game = HemaGame()
        assert (game.computerSelection() != '') == True

    def test_playerWinsComputerWithRockSmashesPaper(self):
        game = HemaGame()
        user_action = "rock"
        computer_action = "scissors"
        assert (game.isWin(user_action, computer_action) == True)


if __name__ == "__main__":
    unittest.main()
