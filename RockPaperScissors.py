import random

while True:
    #inputs
    comp_list = ["Rock", "Paper", "Scissors"]
    user = input("Please choose an option: ").capitalize()
    if user in comp_list:
        pass
    else :
        print("You have given an incorrect input")
        continue  # if user gives incorrect input the program loops back to line 5
    comp = random.choice(comp_list)  # cpu chooses randomly from comp_list

    #print
    print(f"You choose {user}")
    print(f"Computer choose {comp} \n")

    #main
    if user == "Rock" and comp == "Scissors":
        print("You win!")
    elif user == "Rock" and comp == "Paper":
        print("Computer wins!")
    elif user == "Rock" and comp == "Rock":
        print("It's a tie!")
    elif user == "Paper" and comp == "Scissors":
        print("Computer wins!")
    elif user == "Paper" and comp == "Rock":
        print("You Win!")
    elif user == "Paper" and comp == "Paper":
        print("It's a Tie!")
    elif user == "Scissors" and comp == "Rock":
        print("Computer Wins!")
    elif user == "Scissors" and comp == "Paper":
        print("You wins!")
    elif user == "Scissors" and comp == "Scissors":
        print("It's a tie!")
    repeat = input("Do you want to continue? (Y/N)").capitalize()

    if "Y" in repeat:
        continue
    else:
        exit()