students=[
    {"name":"Hermonie", "house":"Gryffindor"},
    {"name": "Harry", "house":"Gryffindor"},
    {"name": "Ron", "house":"Gryffindor"},
    {"name": "Dracoy", "house":"Sltyherin"}
]
# gryffindor = [
#     student["name"] for student in students if student["house"]=="Gryffindor"
# ]

# for gryffindor in sorted(gryffindor):
#     print(gryffindor)

# def is_gryffindor(s):
#     return s["house"]=="Gryffindor"
# gryffindors = filter(is_gryffindor,students)

# for gryffindor in sorted(gryffindors,key=lambda s:s["name"]):
#     print(gryffindor["name"])

students=["Hermonie", "Harry", "Ron"]

gryffindor={ student : "Gryffindor" for student in students}
print(gryffindor)