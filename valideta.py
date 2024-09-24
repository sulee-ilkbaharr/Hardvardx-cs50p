email = input("What is your e mail?").strip()

username, domain = email.split("@")

if (username) and email.endswith(".edu"):
    print("Valid")
else:
    print("Invalid")
