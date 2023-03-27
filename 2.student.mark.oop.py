<<<<<<< HEAD
import sys
import os
import textwrap

class Student:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_dob(self):
        return self.dob

    def set_id(self, id):
        self.id = id

    def set_name(self, name):
        self.name = name

    def set_dob(self, dob):
        self.dob = dob

class Course:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def set_id(self, id):
        self.id = id

    def set_name(self, name):
        self.name = name

class Mark:
    def __init__(self, student, course, mark):
        self.student = student
        self.course = course
        self.mark = mark

    def get_student(self):
        return self.student

    def get_course(self):
        return self.course

    def get_mark(self):
        return self.mark

    def set_student(self, student):
        self.student = student

    def set_course(self, course):
        self.course = course

    def set_mark(self, mark):
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


=======
import os
import sys

# Class Info is the parent class of Student and Courses class
class Info:
    def __init__(self, ID: str, name: str):
        self.ID = ID
        self.name = name
    
    def getID(self):
        return self.ID
    
    def getName(self):
        return self.name
    
    def display(self):
        print("ID: ", self.ID, "Name: ", self.name)

# Class Student is the child class of Info class included one more attributres: dob
class Student(Info):
    def __init__(self, ID: str, name: str, dob: str):
        Info.__init__(self, ID, name)
        self.dob = dob
    
    def getDOB(self):
        return self.dob
    
    def display(self):
        print("ID: ", self.ID, "Name: ", self.name, "DOB: ", self.dob)
        print("\n")

# Class Courses is the child class of Info class included one more attributres: mark
class Courses(Info):
    def __init__(self, ID: str, name: str, mark: int):
        Info.__init__(self, ID, name)
        self.mark = mark
    
    def getMark(self):
        return self.mark
    
    def setMark(self, mark: int):
        self.mark = mark
    
    def display(self):
        print("ID: ", self.ID, "Name: ", self.name, "Mark: ", self.mark)

# Class MarkSheet will contain instances of class Course and class Student.
# It will also contain a list of courses and a list of students
class MarkSheet:
    def __init__(self):
        self.courses = []
        self.students = []
    
    def addCourse(self, course: Courses):
        self.courses.append(course)
    
    def addStudent(self, student: Student):
        self.students.append(student)
    
    def display(self):
        print("Student list: ")
        for student in self.students:
            student.display()
        print("Course list: ")
        for course in self.courses:
            course.display()

# Main function, enter from keyboard
def main():
    marksheet = MarkSheet()
    while True:
        print("1. Add student")
        print("2. Add course")
        print("3. Display")
        print("4. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            ID = input("Enter student ID: ")
            name = input("Enter student name: ")
            dob = input("Enter student dob: ")
            student = Student(ID, name, dob)
            marksheet.addStudent(student)
        elif choice == 2:
            ID = input("Enter course ID: ")
            name = input("Enter course name: ")
            mark = int(input("Enter course mark: "))
            course = Courses(ID, name, mark)
            marksheet.addCourse(course)
        elif choice == 3:
            marksheet.display()
        elif choice == 4:
            break
        else:
            print("Invalid choice")
            sys.exit(0)

if __name__ == "__main__":
    main()
>>>>>>> ecbc8a29a007deffcd0df6149f2e682c19b0e9a7
