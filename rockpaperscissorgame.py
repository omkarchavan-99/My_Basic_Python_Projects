
import random
item_list = ["Rock", "Paper", "Scissor"]

user_choice = input("Enter Your Move = Rock, Paper, or Scissor : ").capitalize()
comp_choice = random.choice(item_list)

print(f"user choice = {user_choice}, \ncomputer choice = {comp_choice}")
if user_choice == comp_choice:
    print("Both chooses same: = Match Tie")

elif user_choice == "Rock":
    if comp_choice == "Paper":
        print("Paper Covers Rock, Computer Win")
    else:
        print("Rock Smashes Scissor, You Win")
elif user_choice == "Paper":
    if comp_choice == "Scissor":
        print("Scissor Cuts Paper, Computer Win")
    else:
        print("Paper Covers Rock, You Win")

elif user_choice == "Scissor":
    if comp_choice == "Paper":
        print("Scissor Cuts Paper, You Win")
    else:
        print("Rock Smashes Scissor, Computer Win")

