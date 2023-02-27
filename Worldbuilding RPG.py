# my code
health = 20
x = 1
y = 1

# +1 for finding a piece of food
    elif (x == 2 and y == 2) or (x == 3 and y == 7) or (x == 5 and y == 4) or (x == 5 and y == 8): # +1 Food
        print("Do you want to open it?: ")
        print("\nA. Yes")
        print("B. No")
        user_choice=input().upper()

        if user_choice.upper()=="A":
            health+=1
            print("\nCongratulations! You found a piece of food.")
            print(f"Health: {health}")
        elif user_choice.upper()== "B":
            print("That’s too bad, you’ve lost a piece of food.")
            print(f"Health: {health}")
    
# +3 for finding a treasure chest full of food
    elif (x == 2 and y == 5) or (x == 6 and y == 4): # +3 Food
        print("Do you want to open it?: ")
        print("\nA. Yes")
        print("B. No")
        user_choice=input().upper()

        if user_choice.upper()=="A":
            health+=3
            print("\nCongratulatons! You found a treasure chest full of food.")
            print(f"Health: {health}")
        elif user_choice.upper()== "B":
            print("That's too bad, you've lost a treasure chest full of food.")
            print(f"Health: {health}")

# +5 finding and eating a magical fruit
    elif (x == 2 and y == 6) or (x == 5 and y == 9) or (x == 7 and y == 4) or (x == 7 and y == 8) or (x == 8 and y == 7): # +5 Food
        print("Do you want to find it?: ")
        print("\nA. Yes")
        print("B. No")
        user_choice=input().upper()

        if user_choice.upper()=="A":
            health+=5
            print("\nCongratulations! You found a magical fruit.")
            print(f"Health: {health}")
        elif user_choice.upper()=="B":
            print("That's too bad, you've lost a magical fruit.")
            print(f"Health: {health}")

# +10 for finding the Fancy Gisele, a magic potion
    elif (x == 4 and y == 3) or (x == 9 and y == 2): # +10 POTION
      print("Emma: You see some potion-like liquid in a fancy bottle on the ground.")
      print("Do you want to drink it?: ")
      print("A. Yes")
      print("B. No")
      user_choice=input().upper()

      if user_choice.upper()=="A":
        health+=10
        print("\nCongratulatons! You found Fancy Gisele, the magic potion.")
        print(f"Health: {health}")
      elif user_choice.upper()=="B":
        print("Emma: That's too bad, you've lost a magic potion.")
        print(f"Health: {health}")

# Lost health by:
# -1 eating poisoned food
    elif (x == 3 and y == 4) or (x == 4 and y == 9) or (x == 6 and y == 8) or (x == 8 and y ==3) or (x == 9 and y == 5): # -1 Food
        print("You see some food. Would you like to eat it: ")
        print("\nA. Yes")
        print("B. No")
        user_choice=input().upper()

        if user_choice.upper()=="A":
            health-=1
            print("\nThe food makes your stomach hurt. Guess it was poisoned.")
            print(f"Health: {health}")
        elif user_choice.upper()=="B":
            print("Oh well. Keep going then.")
            print(f"Health: {health}")
