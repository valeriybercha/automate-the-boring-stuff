# Python practice exercises
# Course: Automate the Boring Stuff with Python
# Developer: Valeriy B.

# Intro

passwordFile = open('secretPasswordFile.txt')
secretPassword = passwordFile.read()
yourPassword = input("Type the pasword: ")
if yourPassword == secretPassword:
    print("Access granted")
    if yourPassword == "12345":
        print ("That password is not good at all")
else:
    print("Access denied")