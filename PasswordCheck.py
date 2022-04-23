# A program that compares two passwords entered by the user
password = input("Create a password")

password1 = input("Enter your password: ")
password2 = input("Enter your password again: ")

if password1 == password2 and password2 == password:
    print("Access granted...")
else:
    print("Access denied. Contact your system administrator.")
