class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing Name")
        if house not in ["Gryffindor","Hulffleuf","Ravenclaw","Slytherin"]:
            raise ValueError("Invalid house")
        self.name=name
        self.house=house
    
    def __str__(self):
        return f"{self.name} from {self.house}"
        
def main():
    student=get_student()
    print(f"{student.name} from {student.house}")

def get_student():
    name=input("Name: ")
    house= input("House:")
    return Student(name,house)

if __name__ == "__main__":
    main()
    