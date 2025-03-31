import random

def divide_gold():
   total_coins = random.randint(1, 1000)
   print(f"Found {total_coins} gold coins!")


   try:
       team_size = int(input("Enter the number of people in the team: "))
       print(f"Each team member gets {total_coins // team_size} coins.")
   except (ValueError, ZeroDivisionError) as e:
       print("Error!", "Invalid input." if isinstance(e, ValueError) else "Cannot divide by zero.")
   finally:
       print("The adventure continues!")




if __name__ == "__main__":
   divide_gold()
