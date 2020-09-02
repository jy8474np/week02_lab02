from dataclasses import dataclass

def main():

    @dataclass
    class Student:
        name: str
        college_id: str
        gpa: float
        
    scott = Student("Scott Summers", "X19631", 3.5)
    henry = Student("Henry McCoy", "X19632", 4.0)
    jean = Student("Jean Grey", "X19633", 3.75)
    bobby = Student("Bobby Drake", "X19634", 3.0)

    print(scott, henry, jean, bobby)
    
main()
