import random




def safe_crack_game():
   secret_code = random.randint(100, 999) 
   attempts = 5  # Number of attempts


   print("Welcome to the game! You need to crack the safe code.")


   while attempts > 0:
       try:
           guess = int(input("Enter a three-digit code: "))


           if guess == secret_code:
               print("Congratulations! You cracked the safe code!")
               return
           print("The code is higher." if guess < secret_code else "The code is lower.")


       except ValueError:
           print("Error! Please enter a number.")


       finally:
           attempts -= 1
           print(f"Attempts left: {attempts}")


   print(f"Game over. The correct code was: {secret_code}")
safe_crack_game()
