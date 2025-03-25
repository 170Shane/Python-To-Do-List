user_input = input("Type the name of the member you want to add: ")

with open("files/members.txt", "a") as file:
    file.write(user_input + "\n")
    
