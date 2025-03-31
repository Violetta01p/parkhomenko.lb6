import random


choices = ["rock", "scissors", "paper", "lizard", "spock"]


rules = {
   "rock": ["scissors", "lizard"],
   "scissors": ["paper", "lizard"],
   "paper": ["rock", "spock"],
   "lizard": ["paper", "spock"],
   "spock": ["scissors", "rock"]
}


def determine_winner(user_choice, computer_choice):
   if user_choice == computer_choice:
       return "It's a tie!"
   elif computer_choice in rules[user_choice]:
       return "You win!"
   else:
       return "You lose!"


def play_game():
   print("Choose: rock, scissors, paper, lizard, spock")




   user_choice = input("Your choice: ").lower()


   if user_choice not in choices:
       print("Invalid choice! Try again.")
       return


   computer_choice = random.choice(choices)
   print(f"Computer chose: {computer_choice}")


   result = determine_winner(user_choice, computer_choice)
   print(result)


play_game()
