


    user_choice = input("Enter rock, paper, or scissors: ") 
     user_choice  ["rock", "paper", "scissors"]:
        print("Invalid input. Please choose 'rock', 'paper', or 'scissors'.")
    

    computer_choice = random.choice(["rock", "paper", "scissors"])
    print(f"Computer chose {computer_choice}")

     user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or 
         (user_choice == "scissors" and computer_choice == "paper") or 
         (user_choice == "paper" and computer_choice == "rock"):
        print("You win!")
    else:
        print("You lose!")


