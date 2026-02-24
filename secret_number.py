from module import isdigit
from os import system
system("clear")

secret_number = 333

print("Autheticating user...")
pwd = input("What's the secret number? ")
print()

if pwd == 333:
    print("Success! Opening RESTRICTED APP...")
else:
    print("That's the wrong number.")