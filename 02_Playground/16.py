"""Demonstrate inheritance with Person, Student, and Teacher classes."""


class Person:
    def __init__(self, name, age=18, gender="m"):
        self.name = name
        self.age = age
        self.gender = gender

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)

    def work(self):
        pass


class Student(Person):
    def work(self):
        print(f"{self.name} is studying.")


class Teacher(Person):
    def work(self):
        print(f"{self.name} is teaching.")


student_name = input("Enter student name: ")
student_age = input("Enter student age (default 18): ")
student_gender = input("Enter student gender (default m): ")
student = Student(
    student_name,
    int(student_age) if student_age else 18,
    student_gender or "m",
)
student.display()
student.work()

teacher_name = input("Enter teacher name: ")
teacher_age = input("Enter teacher age (default 18): ")
teacher_gender = input("Enter teacher gender (default m): ")
teacher = Teacher(
    teacher_name,
    int(teacher_age) if teacher_age else 18,
    teacher_gender or "m",
)
teacher.display()
teacher.work()
