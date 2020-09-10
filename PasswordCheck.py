# A program that compares two passwords entered by the user

password1 = input("Enter your password: ")
password2 = input("Enter your password again: ")

if password1 == password2:
    print("Access granted...")
else:
    print("Access denied. Contact your system administrator.")
