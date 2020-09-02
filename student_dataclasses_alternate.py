from dataclasses import dataclass # Import dataclass

def main():

    @dataclass # Define dataclass and its data types
    class Student:
        name: str
        college_id: str
        gpa: float
    
    # Student data
    scott = Student("Scott Summers", "X19631", 3.5)
    henry = Student("Henry McCoy", "X19632", 4.0)
    jean = Student("Jean Grey", "X19633", 3.75)
    bobby = Student("Bobby Drake", "X19634", 3.0)

    # Display students' details
    print(scott)
    print(henry)
    print(jean)
    print(bobby)
    
main()
