"""
Creates Student objects
Assigns each student a random grade (0–10)
Prints all grades
Calculates and prints the average
import random
"""
class Student:
    def __init__(self, fullname):
        self.fullname = fullname
        self.grade = -1

def grade_student(student):
    student.grade = random.randint(0, 10)


def average(lista):
    sum_grade = 0
    for student in lista:
        sum_grade += student.grade
    print(f"The average of the Students grade is: {sum_grade / len(lista)}")


students = [
    "Alex Johnson",
    "Maria Gonzalez",
    "Daniel Thompson",
    "Emily Chen",
    "Michael Brown",
    "Sophia Martinez",
    "James Wilson",
    "Aisha Rahman",
    "Benjamin Carter",
    "Olivia Anderson"
]
total_students = [Student(student) for student in students]

for student in total_students:
    grade_student(student)

for student in total_students:
    print(student.grade)
average(total_students)