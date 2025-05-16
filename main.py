import pygame
import sys
from game import Game


def main():
    pygame.init()
    game = Game()
    print("Trạng thái ban đầu:")
    for row in game.start:
        print(row)
    print("\nTrạng thái đích:")
    for row in game.goal:
        print(row)
    game.run()


if __name__ == "__main__":
    main()
