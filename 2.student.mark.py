import sys
import os
import textwrap

class Student:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob

class Course:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Mark:
    def __init__(self, student, course, mark):
        self.student = student
        self.course = course
        self.mark = mark

students = []
courses = []
marks = []

def add_student():
    print("Add a student")
    id = input("Enter student id: ")
    name = input("Enter student name: ")
    dob = input("Enter student date of birth: ")
    student = Student(id, name, dob)
    students.append(student)
    print("Student added successfully")

def add_course():
    print("Add a course")
    id = input("Enter course id: ")
    name = input("Enter course name: ")
    course = Course(id, name)
    courses.append(course)
    print("Course added successfully")

def add_mark():
    print("Add a mark")
    student_id = input("Enter student id: ")
    course_id = input("Enter course id: ")
    mark = input("Enter mark: ")
    student = None
    course = None
    for s in students:
        if s.id == student_id:
            student = s
            break
    for c in courses:
        if c.id == course_id:
            course = c
            break
    if student is not None and course is not None:
        mark = Mark(student, course, mark)
        marks.append(mark)
        print("Mark added successfully")
    else:
        print("Student or course not found")

def list_students():
    print("List students")
    print("Id\tName\tDate of birth")
    for s in students:
        print(s.id + "\t" + s.name + "\t" + s.dob)

def list_courses():
    print("List courses")
    print("Id\tName")
    for c in courses:
        print(c.id + "\t" + c.name)

def list_marks():
    print("List marks")
    print("Student\tCourse\tMark")
    for m in marks:
        print(m.student.name + "\t" + m.course.name + "\t" + m.mark)

def print_menu():
    print("Student mark management system")
    print("1. Add a student")
    print("2. Add a course")
    print("3. Add a mark")
    print("4. List students")
    print("5. List courses")
    print("6. List marks")
    print("7. Exit")

def main():
    while True:
        print_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            add_student()
        elif choice == "2":
            add_course()
        elif choice == "3":
            add_mark()
        elif choice == "4":
            list_students()
        elif choice == "5":
            list_courses()
        elif choice == "6":
            list_marks()
        elif choice == "7":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()


