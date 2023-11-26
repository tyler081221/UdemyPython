# 피자 주문 실습 (다중 연속 if문)

print("Thank you for choosing python Pizza Deliveries!")

size = input("Pizza Size S, M, L? ")
add_pepperoni = input("Add Pepperoni Y or N? ")
extra_cheese = input("Extra cheese Y or N? ")

if size == "S":
    bill = 15
    if add_pepperoni == "Y":
        bill += 2
        if extra_cheese == "Y":
            bill += 1
            print(f"Your bill is ${bill}.")
        else:
            print(f"Your bill is ${bill}.")
    else:
        if extra_cheese == "Y":
            bill += 1
            print(f"Your bill is ${bill}.")
        else:
            print(f"Your bill is ${bill}.")
elif size == "M":
    bill = 20
    if add_pepperoni == "Y":
        bill += 3
        if extra_cheese == "Y":
            bill += 1
            print(f"Your bill is ${bill}.")
        else:
            print(f"Your bill is ${bill}.")
    else:
        if extra_cheese == "Y":
            bill += 1
            print(f"Your bill is ${bill}.")
        else:
            print(f"Your bill is ${bill}.")
else:
    bill = 25
    if add_pepperoni == "Y":
        bill += 3
        if extra_cheese == "Y":
            bill += 1
            print(f"Your bill is ${bill}.")
        else:
            print(f"Your bill is ${bill}.")
    else:
        if extra_cheese == "Y":
            bill += 1
            print(f"Your bill is ${bill}.")
        else:
            print(f"Your bill is ${bill}.")