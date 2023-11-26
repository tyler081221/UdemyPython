#   BMI 2.0

print("Welcome to BMI Calculator 2.0 !")

height = float(input("Height? (m) "))
weight = int(input("Weigth? (kg) "))

BMI = weight / height ** 2

if BMI < 18.5:
    print(f"Your BMI is {BMI}. Underweight.")
elif BMI < 25:
    print(f"Your BMI is {BMI}. Normal weight.")
elif BMI < 30:
    print(f"Your BMI is {BMI}. Slightly overweight.")
elif BMI < 35:
    print(f"Your BMI is {BMI}. Obese.")
else:
    print(f"Your BMI is {BMI}. Clinically obese.")


# 롤러코스터 입장 조건 2.0

# height = int(input("Type your height cm. "))

# if height >= 120:
#     print("You can ride!")
#     age = int(input("Type your age. "))
#     if age < 12:
#         print("Pay $5.")
#     elif age <= 18:
#         print("Pay $7.")
#     else:
#         print("Pay $12.")
# else:
#     print("You can't ride.")