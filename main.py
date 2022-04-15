import random


class Player:
    def __init__(self):
        self.score = 0
        pass


def decide():
    turn = random.randint(0, 2)
    return turn


if __name__ == '__main__':
    ROCK = 0
    PAPER = 1
    SCISSSOR = 2
    play = decide()
    print(play)

# USE OOPS for players