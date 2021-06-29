import random
guess=random.randint(0,100)
print("I'm thinking a number between 0 and 100, Guess now!")
level=input("How do you want to play this game? easy or hard?\n")
level=level.lower()
attempt=1
if level=="easy":
  while attempt<=10:
    #Code
    print(f"You have {10-attempt+1} attempts ")
    user_guess=int(input("Guess the number"))
    attempt+=1
    if user_guess!=guess:
      if user_guess<guess:
        print("Too low")
      else:
        print("Too high")
    else:
      print("You win!")
      break
    if(attempt==10):
      print("Game over!")
      break
else:
  while attempt<=5:
    print(f"You have {5-attempt+1} attempts ")
    user_guess=int(input("Guess the number: \n"))
    attempt+=1
    if user_guess!=guess:
      if user_guess<guess:
        print("Too low")
      else:
        print("Too high")
    else:
      print("You win!")
      break
    if(attempt==10):
      print("Game over!")
      break
