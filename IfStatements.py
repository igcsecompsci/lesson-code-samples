# Use of if statements

# Check if a number is less than another number
if 20 > 15:
  print("20 is greater than 15.")
else:
  print("20 is not greater than 15.")
  
  
# Check if a number is the same as another number
if 20 == 20:
  print("Both numbers are the same.")
else:
  print("Both numbers are different.")


# Checking a person's age using a variable
age = 16

if age >= 16:
  print("You are old enough to watch the movie.")
else:
  print("You are too young to watch the movie.")
  
  
# A program that simulates traffic lights using if-elif-else

light = input("What colour is the light?: ")

if light == "Red":
    print("The light is {}. You should stop.".format(light))
elif light == "Orange":
    print("The light is {}. You should wait.".format(light))
else:
    print("The light is {}. You can go.".format(light))
  
