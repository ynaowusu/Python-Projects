#figure out how to pick a random name from the list of friends
 
import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

rand_int = random.randint(0, 4)

if rand_int == 0:
    print("Alice should pay the bill")
elif rand_int == 1:
    print("Bob should pay the bill")
elif rand_int == 2:
    print("Charlie should pay the bill")
elif rand_int == 2:
    print("David should pay the bill")
else:
    print("Emanuel should pay the bill")




