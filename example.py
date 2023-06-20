
import random


def game():
    while True:
        choices = ['stone', 'paper', 'scissors']

        computer = random.choice(choices)
        player = None

        while player not in choices:
            player = input("stone, paper or scissors : ").lower()

        if player == computer:
            print("Player:", player)
            print("Computer:", computer)
            print("Tie !")

        elif player == 'stone':
            if computer == 'paper':
                print("Player:", player)
                print("Computer:", computer)
                print("Computer wins !")

            if computer == 'scissors':
                print("Player:", player)
                print("Computer:", computer)
                print("player wins !")

        elif player == 'paper':
            if computer == 'scisssors':
                print("Player:", player)
                print("Computer:", computer)
                print("Computer wins !")

            if computer == 'stone':
                print("Player:", player)
                print("Computer:", computer)
                print("player wins !")

        elif player == 'scissors':
            if computer == 'stone':
                print("Player:", player)
                print("Computer:", computer)
                print("Computer wins !")

            if computer == 'paper':
                print("Player:", player)
                print("Computer:", computer)
                print("player wins !")
        play_again = input("Play again ? (yes/no): ").lower()

        if play_again != 'yes':
            break
