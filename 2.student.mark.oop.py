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