# Students list that hlds the dict
students =[
   {"name":"Hermonie","House":"Gryfindor","patronus":"Otter"},
   {"name":"Harry","House":"Gryfindor","patronus":"Stag"},
   {"name":"Ron","House":"Gryfindor","patronus":"Jack Russel Terrier"},
   {"name":"Draco","House":"Slytherin","patronus":None} 
]
for student in students:
     print(student)
     
     
for student in students:
     print(student["name"], student["House"],student["patronus"] ,sep=",")