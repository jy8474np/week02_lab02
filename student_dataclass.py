from dataclasses import dataclass

def main():
    
    class Student:
        def __init__(self, name, college_id, gpa):
            self.name = name
            self.college_id = college_id
            self.gpa = gpa
        
        def __str__(self):
            return f"Student Name: {self.name} College ID: {self.college_id} GPA: {self.gpa}"

    scott = Student("Scott Summers", 19631 , 3.5)
    henry = Student("Henry McCoy", 19632, 4.0)
    jean = Student("Jean Grey", 19633, 3.75)
    bobby = Student("Bobby Drake", 19634, 3.0)

    print(scott, henry, jean, bobby)
main()