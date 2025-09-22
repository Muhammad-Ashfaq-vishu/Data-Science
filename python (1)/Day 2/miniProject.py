password = input("Enter your password: ")

if len(password) < 8:
    print("Too short! Password must be at least 8 characters.")
elif " " in password:
    print("Password should not contain spaces.")
elif not any(ch.isdigit() for ch in password):   # optional rule
    print("Password should contain at least one number.")
else:
    print("Password Accepted ✅")
