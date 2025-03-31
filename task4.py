try:
   score = int(input("Enter the number of points earned (from 0 to 100): "))


   if score < 0 or score > 100:
       raise ValueError("Invalid input! The number of points must be between 0 and 100")
   if score < 50:
       rating = "Beginner"
       multiplier = 1
   elif score < 70:
       rating = "Silver Player"
       multiplier = 1.5
   elif score < 90:
       rating = "Gold Player"
       multiplier = 2
   else:
       rating = "Platinum Player"
       multiplier = 3


   final_score = score * multiplier
   print(f"Your rating: {rating}! You earned {final_score} points (multiplier ×{multiplier})!")


except ValueError as e:
   print(e)
