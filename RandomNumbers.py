# Generate random numbers between 1-5

import random

# Output a single random number
number = random.randint(1, 5)
print(number)

# Output another 5 random numbers
count = 0
while(count < 5):
  number = random.randint(1, 5)
  print(number)
  count += 1
