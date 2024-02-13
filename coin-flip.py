# In the `coin-flip.py` file, we will write some code to accomplish the following:
import random
# 1. Let’s simulate flipping 100 coins and output the results.
heads = 0
tails = 0
for flip in range(100):  # range(0,100,1) # range (0,100)
    coin = random.randint(1, 2)
    if (coin == 1):
        print("heads")
        heads += 1  # heads = heads + 1
    else:
        print("tails")
        tails += 1  # tails count also goes up
print(f"After 100 flips, we flipped {heads} heads and {tails} tails")


# 2. Now, let’s keep count of how many heads and tails we flipped.
