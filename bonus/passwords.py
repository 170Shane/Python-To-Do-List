password = input("Enter the password: ")

if len(password) >= 8 and any(char.isdigit() for char in password) and any(char.isupper() for char in password):
    print("Password is valid.")
else:
    print("Password is invalid. It must be at least 8 characters long, contain at least one digit, and contain at least one uppercase letter.")
    
a = {}
for key, value in a.items():
    print(f"{key}: {value}")    
    
    