# #ask user for their name
# name = input("whats your name?").strip().title()
# #remove whitespace from str
# name = name.strip().title()

# #capitiliza the name
# name= name.title()
# first, last = name.split()
# name = name.capitalize()
# print(f"hello, {first}" ) 


def hello(to="world"):
    print("hello, ", to)

hello()    
to=input("what is your name")
hello(to)
