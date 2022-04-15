import random

ROCK = 0
PAPER = 1
SCISSOR = 2


class Game:
    def __init__(self):
        self.moves_history = []

    def decider(self):
        pass

class Player:
    def __init__(self):
        self.score = 0
        self.moves_history = []
        pass

    def count_moves(self):
        pass

    def count_score(self):
        self.score += 1


def roll_hand():
    turn = random.randint(0, 2)
    return turn


if __name__ == '__main__':
    player_1 = Player()
    player_2 = Player()

    while True:
        break

    play = roll_hand()
    print(play)

# USE OOPS for players