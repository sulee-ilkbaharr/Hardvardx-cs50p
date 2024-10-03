import csv 

def add_student(name, surname, email, birthday):
    with open("students.csv", "a" ,"") as  file:
        writer=csv.writer(file)
        writer.writerow([name, surname, email, birthday])