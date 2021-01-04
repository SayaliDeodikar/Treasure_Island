print("********WELCOME TO TREASURE ISLAND.**********")
print("Your mission is to find the treasure.") 
dir = input("You are at the cross road. Where would you like to go? Left or Right: ")
if dir == "right" or dir == "Right" :
    dis = input("Level 1 cleared! You are at river. Take Boat or Swim. Type 'Boat' for taking a boat. Type 'Swim' for Swimming: ")
    if dis == 'Boat':
        door=input("You are close to the treasure. Choose one door. Red, Blue or Yellow?: ")
        if door == 'Yellow' or door == 'yellow': 
            print("Yay!! Congratulations!! You found the treasure!")
        elif door == 'Red' or door =='red':
            print("Wrong door! Caught by police. GAME OVER!")
        elif door == 'Blue' or door == 'blue': 
            print("Wrong door! Fire. GAME OVER!")
    elif dis == 'Swim':
        print("Crocodiles Attack! GAME OVER!")
else:
    print("You met an accident. GAME OVER!")
