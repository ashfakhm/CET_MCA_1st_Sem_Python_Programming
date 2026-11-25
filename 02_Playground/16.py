"""
Student Class

This program creates a student object and displays its details.
"""


class Student:
    def __init__(self, name, age=18, gender="m"):
        self.name = name
        self.age = age
        self.gender = gender

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)


name = input("Enter student name: ")
age = input("Enter student age (default 18): ")
gender = input("Enter student gender (default m): ")

student = Student(name, int(age) if age else 18, gender or "m")

student.display()
