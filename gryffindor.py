students=[
    {"name":"Hermonie", "house":"Gryffindor"},
    {"name": "Harry", "house":"Gryffindor"},
    {"name": "Ron", "house":"Gryffindor"},
    {"name": "Dracoy", "house":"Sltyherin"}
]
gryffindor = [
    student["name"] for student in students if student["house"]=="Gryffindor"
]

for gryffindor in sorted(gryffindor):
    print(gryffindor)