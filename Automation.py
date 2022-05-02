import random

result = []

for i in range(0, 100):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    dice3 = random.randint(1, 6)
    sum = dice1 + dice2 + dice3
    result.append(sum)

print(result)
