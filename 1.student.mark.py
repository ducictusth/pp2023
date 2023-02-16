import sys
import os
import textwrap

## Create a student mark management system using tuples, lists and dictionaries

students = []
courses = []

# Create a list of students: id, name, dob
def input_students():
    print("Enter student details: ")
    while True:
        id = input("Enter student id: ")
        name = input("Enter student name: ")
        dob = input("Enter student date of birth: ")
        students.append((id, name, dob))
        more = input("Do you want to add more students (y/n)? ")
        if more == 'n':
            break

# Create a list of courses: id, name
def input_courses():
    print("Enter course details: ")
    while True:
        id = input("Enter course id: ")
        name = input("Enter course name: ")
        courses.append((id, name))
        more = input("Do you want to add more courses (y/n)? ")
        if more == 'n':
            break

# Create a dictionary of marks: student_id, course_id, mark
def input_marks():
    marks = {}
    for student in students:
        for course in courses:
            mark = input("Enter mark for student %s in course %s: " % (student[1], course[1]))
            marks[(student[0], course[0])] = mark
    return marks

# Display a list of students
def display_students():
    print("Student list: ")
    for student in students:
        print("ID: %s, Name: %s, DOB: %s" % (student[0], student[1], student[2]))

# Display a list of courses
def display_courses():
    print("Course list: ")
    for course in courses:
        print("ID: %s, Name: %s" % (course[0], course[1]))

# Display a dictionary of marks
def display_marks(marks):
    print("Mark list: ")
    for student in students:
        for course in courses:
            print("Student: %s, Course: %s, Mark: %s" % (student[1], course[1], marks[(student[0], course[0])]))

# Main program
def main():
    print("Student Mark Management System")
    input_students()
    input_courses()
    marks = input_marks()
    display_students()
    display_courses()
    display_marks(marks)

if __name__ == '__main__':
    main()