names = input("what is your name?")
with open("names.txt", "a") as file:
    file.write(f"{names}\n")
    
    

names =[]
with open("names.txt") as file:
    for line in file:
        names.append(line.rsplit())

for name in sorted(names):
    print(f"hello, {name}")

file.close()