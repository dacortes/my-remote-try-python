#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

##from flask import Flask, send_file
#import os
#import pdb
#
#app = Flask(__name__)
#
#@app.route("/")
#def hello():
#    print("init app")
#    message = "¡Hola judador !"
#    pdb.set_trace()
#    static_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'static')
#    index_path = os.path.join(static_dir, 'index.html')
#
#    with open(index_path, 'r') as file:
#        content = file.read()
#        modified_content = content.replace('{{ message }}', message)
#
#    with open('index.html', 'w') as modified_file:
#        modified_file.write(modified_content)
#
#    return send_file('index.html')
#
import random

def game():
    choices = ["rock", "paper", "scissors"]
    player_wins = 0
    rounds_played = 0

    while True:
        player_choice = input("Enter rock, paper, or scissors (or 'quit' to exit): ").lower()

        if player_choice == 'quit':
            break

        if player_choice not in choices:
            print("Invalid choice. Please enter rock, paper, or scissors.")
            continue

        computer_choice = random.choice(choices)
        print(f"Computer chooses: {computer_choice}")

        if player_choice == computer_choice:
            print("It's a tie!")
        elif (player_choice == 'rock' and computer_choice == 'scissors') or \
             (player_choice == 'paper' and computer_choice == 'rock') or \
             (player_choice == 'scissors' and computer_choice == 'paper'):
            print("You win!")
            player_wins += 1
        else:
            print("You lose!")

        rounds_played += 1

    print(f"Game ended. You won {player_wins} out of {rounds_played} rounds.")

if __name__ == "__main__":
    game()
