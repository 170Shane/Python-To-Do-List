# password = input("Enter your password: ")
# if password == "secret":
#     print("Correct!")
# else:
#     print("Incorrect!")

password = input("Enter your password: ")
while password != "secret":
    print("Incorrect!")
    password = input("Enter your password: ")
else:
    print("Correct!")
