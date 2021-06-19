from art import logo, vs
from game_data import data
import random
import os

def format_data(account):
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:

#Generating a randoom account from the game data
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")


    #Ask user for a guess
    guess = input("Who has more followers? Give your choice 'A' or 'B': ").lower()

    ##Get follower count of each account

    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    os.system('cls')  #Clear the screen between rounds

    #Giver user feedback on their guess
    if is_correct:
        score += 1
        print(f"You are right! Current score is: {score}.")
    else:
        game_should_continue = False
        print(f"Sorry, Better luck next time! Final score is: {score}.")


