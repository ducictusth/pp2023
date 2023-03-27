import os
import sys
import math

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
    
    # Set mark using math()function
    def setMark(self, std_list: list, mark: int):
        for std in std_list:
            f_mark = float(input("Enter mark for student " + std.getName() + ": "))
            i_mark = math.floor(f_mark)
            self.__marks.append(i_mark)

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

    def listCourse(self):
        for course in self.courses:
            course.display()
    
    def listStudent(self):
        for student in self.students:
            student.display()

    def calculateGpa(self, std_list: list, course_list: list):
        # Create a table display GPA for each student
        print("Student list: ")
        for std in std_list:
            std.display()
        print("Course list: ")
        for course in course_list:
            course.display()
        print("GPA table: ")
        for std in std_list:
            print("Student: ", std.getName())
            for course in course_list:
                print("Course: ", course.getName())
                print("Mark: ", course.getMark())
                print("GPA: ", course.getMark()/10)
            print("\n")

    def sortGpa(self, std_list: list, course_list: list):
        gpa_sorted = sorted(std_list, key=lambda std: std.getMark()/10, reverse=True)
        gpa_sorted.reverse()
        return gpa_sorted

    
    def display(self):
        print("Course list: ")
        for course in self.courses:
            course.display()
        print("Student list: ")
        for student in self.students:
            student.display()
        print("\n")

# Main function, enter from keyboard to show the result including the marks and GPA of each student.
def main():
    ms = MarkSheet()
    while True:
        print("Student Management System")
        print("1. Add student")
        print("2. Add course")
        print("3. List student")
        print("4. List course")
        print("5. Calculate GPA")
        print("6. Sort GPA")
        print("7. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            ID = input("Enter student ID: ")
            name = input("Enter student name: ")
            dob = input("Enter student date of birth: ")
            student = Student(ID, name, dob)
            ms.addStudent(student)
        elif choice == 2:
            ID = input("Enter course ID: ")
            name = input("Enter course name: ")
            mark = float(input("Enter course mark: "))
            course = Courses(ID, name, mark)
            ms.addCourse(course)
        elif choice == 3:
            ms.listStudent()
        elif choice == 4:
            ms.listCourse()
        elif choice == 5:
            ms.calculateGpa(ms.students, ms.courses)
        elif choice == 6:
            ms.sortGpa(ms.students, ms.courses)
        elif choice == 7:
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
