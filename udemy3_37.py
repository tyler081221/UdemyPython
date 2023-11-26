# 사랑 계산기 (논리 연산자)

print("The Love Calculator is calculating your score.")

name1 = input("What is your name? ")
name2 = input("What is their name? ")

score_true_name1 = name1.count('t') + name1.count('r') + name1.count('u') + name1.count('e')
score_true_name2 = name2.count('t') + name2.count('r') + name2.count('u') + name2.count('e')
score_love_name1 = name1.count('l') + name1.count('o') + name1.count('v') + name1.count('e')
score_love_name2 = name2.count('l') + name2.count('o') + name2.count('v') + name2.count('e')

score = 10 * (score_true_name1 + score_true_name2) + score_love_name1 + score_love_name2

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")