import random
roll_dice = input("comment start to roll the dice: ")

if roll_dice == "start" or roll_dice=="START":
   posiblle_results = [1, 2, 3, 4, 5, 6]
   result = random.choice(posiblle_results)
   print("Result of dice rolling is : " + str(result))
