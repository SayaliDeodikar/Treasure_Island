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











# if dir == 'left' or 'LEFT' or 'Left' or 'L' or 'l':
#     print("You met an accident. GAME OVER!")
# elif dir == 'right' or 'Right' or 'r' or 'R' or 'Right':
#     dis = input("You have two options. Take Boat or Swim. Type 'Boat' for taking a boat. Type 'Swim' for Swimming")
#     if dis == 'Swim':
#         print("Crocodiles Attack! GAME OVER!")
#     elif dis == 'Boat':
#         door=input("You are close to the treasure. Choose one door. Red, Blue or Yellow?")
#         if door == 'Red' or 'red' or 'RED' or 'R' or 'r':
#             print("Wrong door! Caught by police. GAME OVER!")
#         elif door == 'Blue' or 'blue' or 'BLUE' or 'B' or 'b':
#             print("Wrong door! Fire. GAME OVER!")
#         elif door == 'Yellow' or 'YELLOW' or 'Y' or 'y' or 'yellow': 
#             print("Yay!! Congratulations!! You found the treasure!")