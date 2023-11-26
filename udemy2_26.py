# 팁 계산기

print("Welcome to the tip calculator.")

total_bill = input("What was the total bill? ")
percentage = input("What percentage tip would you like to give? 10, 12, or 15? ")
people_num = input("How many people to split the bill? ")

each_tip = round((float(total_bill) / int(people_num)) * (1 + int(percentage) / 100), 2)

print(f"Each person should pay ${each_tip}.")