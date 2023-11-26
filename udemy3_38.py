# 보물섬

print("Welcome to Treasure Island. Your mission is to find the treasure")

left_right = input("Left or right? ")

if left_right == "left":
    swim_wait = input("Swim or wait? ")
    if swim_wait == "wait":
        door_color = input("Which door red, blue, yellow? ")
        if door_color == "yellow":
            print("You win!")
        else:
            print("Game Over")
    else:
        print("Game Over")
else:
    print("Game Over")



