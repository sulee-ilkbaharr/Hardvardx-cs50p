import csv


#list
students=[]
with open("student.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name":row["name"],"home":row["home"]})
    # for line in file:
    #     name, house= line.strip().split(",")
    #     #dictionay 
    #     student={"name":name, "house":house}
    #     #we can add the dictionary to inside the list
    #     students.append(student)
 
 
# def get_name(student):
#     return student["name"]

     
for student in sorted(students,key=lambda student:student["name"]):
    print(f"{student['name']} is from {student['home']}")
        