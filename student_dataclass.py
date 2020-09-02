# In the slides/lecture, you created the main method after several chunks of code.
# I placed the entirety of my code inside the main method.
# Questions:
# 1. Why wouldn't one want all of their code within the main method?
# 2. What's the difference?
# 3. Is one way much preferred to the other?

from dataclasses import dataclass # Import dataclass

def main():
    
    # Create class and define its components
    class Student:
        def __init__(self, name, college_id, gpa):
            self.name = name
            self.college_id = college_id
            self.gpa = gpa
        
        # Displayed information format
        def __str__(self):
            return f"Student Name: {self.name} College ID: {self.college_id} GPA: {self.gpa} | "

    # Student data
    scott = Student("Scott Summers", 19631 , 3.5)
    henry = Student("Henry McCoy", 19632, 4.0)
    jean = Student("Jean Grey", 19633, 3.75)
    bobby = Student("Bobby Drake", 19634, 3.0)

    print(scott, henry, jean, bobby) # Display students' details

main()