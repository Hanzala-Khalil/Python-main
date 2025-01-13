import random

def get_choices():
    player_choices = input("Enter a choice(rock, paper ,scissors): ")
    options = ["rock","paper","scissors"]
    computer_choices = random.choice(options)
    choices = {"player" : player_choices,"computer":computer_choices}
    result = check_win(choices["player"],choices["computer"])
    return result


def check_win(player,computer):
    print(f"Player chose {player},Computer chose {computer}")
    if player==computer:
        return"tie"
    if player=="rock":
        if computer=="paper":
            return"Paper Beats Rock"
        else:
            return"Rock Beats Scissors"
    if player=="paper":
        if computer=="rock":
            return"Paper Beats Rock"
        else:
            return"Scissors Beats Paper"
    if player=="scissors":
        if computer=="paper":
            return"Scissors Beats Paper"
        else:
            return"Rock Beats Scissors"

result = get_choices()
print(result)
