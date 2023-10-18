import sys
class Student():
    def __init__(self,name,school):
        if not name:
            raise ValueError("No se escribio el nombre")
            #sys.exit()
        
        self.name=name
        self.school =school


def main():
    student = get_student()
    print(f"{student.name} va al colegio {student.school}")
    

def get_student():
    name= input("Name: ")
    school=input("School: ")
    return Student(name,school)

if __name__=="__main__":
    main()