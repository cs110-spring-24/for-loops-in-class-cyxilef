# 2: Dice Roll

# In the `dice-roll.py` file, we will write some code to accomplish the following:
import random
ones = 0
twos = 2
threes = 3
fours = 4
fives = 5
sixes = 6
# 1. Let’s simulate roll 100 dice and print out each dice value
for roll in range(100):
    dice = random.randint(1, 6)
    if dice == 1:
        ones += 1
    elif dice == 2:
        twos += 1
    elif dice == 3:
        threes += 1
    elif dice == 4:
        fours += 1
    elif dice == 5:
        fives += 1
    else:
        sixes += 1
print(dice)
# 2. Now, let’s count how many 1s, 2s, 3s, 4s, 5s, and 6s were rolled

print(f" {ones} 1s, {twos} 2s, {threes} 3s, {fours} 4s, {fives} 5s, {sixes} 6s were present")
