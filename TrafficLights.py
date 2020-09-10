# A program that decides what to do depending on the colour of the traffic light

light = input("What colour is the light?: ")

if light == "Red":
    print("The light is {}. You should stop.".format(light))
elif light == "Orange":
    print("The light is {}. You should wait.".format(light))
else:
    print("The light is {}. You can go.".format(light))
