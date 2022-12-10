import random
option = ("rock", "paper", "scissors")# tupples for our choices 
running=0
while (running<5): # while loop to run 5 times 
   
    running+=1
  
    player = None #storing null value 
    computer = random.choice(option)

    while player not in option: # while our player variable doesnot choose tupples options
        player = input("Enter a choice (rock, paper, scissors): ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "scissors":
        print("You win!")
    elif player == "paper" and computer == "rock":
        print("You win!")
    elif player == "scissors" and computer == "paper":
        print("You win!")
    else:
        print("You lose!")
print("Thanks for playing!")
