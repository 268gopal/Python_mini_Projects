import random
item_list = ["Rock", "Paper", "Scissor"]

user_choice = input("Enter your choice(Rock, Paper, Scissor) :").title()
comp_choice = random.choice(item_list)


if(user_choice.title() == comp_choice.title() ):
    print(f"You choose {user_choice} and computer choose {comp_choice} . \n So it's a tie")
elif user_choice == 'Rock':
    if comp_choice == 'Paper':
        print(f"you had Chosen {user_choice} and computer chosen {comp_choice}.\n So computer Wins.")
    else:
        print(f"you had Chosen {user_choice} and computer chosen {comp_choice}.\n So You Win.")
elif user_choice == 'Paper':
    if comp_choice == 'Scissor':
        print(f"you had Chosen {user_choice} and computer chosen {comp_choice}.\n So computer Wins.")
    else:
        print(f"you had Chosen {user_choice} and computer chosen {comp_choice}.\n So you Win.")
elif user_choice == 'Scissor':
    if comp_choice == 'Rock':
        print(f"you had Chosen {user_choice} and computer chosen {comp_choice}.\n So computer Wins.")
    else:
        print(f"you had Chosen {user_choice} and computer chosen {comp_choice}.\n So you Win.")