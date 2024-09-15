name = input("what is your name ?")
fromm= input("where are u from?")
with open("student.csv", "a") as file:
    file.write(f"{name},{fromm}\n")
        
