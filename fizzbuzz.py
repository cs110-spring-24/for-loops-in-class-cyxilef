# In the `fizzbuzz.py` file, we will write some code to simulate the Fizz Buzz problem.

# Instruction

# 1. Print out all the numbers between 1 and 30
for count in range(1, 31):
    if count % 15 == 0:
        print("FizzBuzz")
    elif count % 3 == 0:
        print("Fizz")
    elif count % 5 == 0:
        print("Buzz")
    else:
        print(count)


# 2. If the number is a multiple of 3, instead of printing the number, print out “Fizz”
# 3. If the number is a multiple of 5, instead of printing the number, print out “Buzz”
# 4. If the number is a multiple of 15, instead of printing the number, print out “FizzBuzz”
