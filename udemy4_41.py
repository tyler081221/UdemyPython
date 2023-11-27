# Random 연습 (동전 던지기)

import random

random_coin = random.randint(0,1)

if random_coin == 1:
    print("앞면")
else:
    print("뒷면")


# Random 모듈

# import random

# random_integer = random.randint(1,10)
# print(random_integer)

# random_float = random.random() * 5
# print(random_float)

# love_score = random.randint(1, 100)
# print(f"Your love score is {love_score}.")