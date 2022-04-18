import math
from domains.student import *
from domains.course import *
from domains.mark import *
from domains.StdManagement import *

def getNumOfStudents():
        while True:
            number_std = int(input("\nEnter number of students: "))
            if number_std < 0:
                print("\nNumber of students cannot be negative")
            else:
                break
        StdManagement.number_std = number_std

def getNumOfCourses():
        while True:
            num_of_courses = int(input("\nEnter number of courses: "))
            if num_of_courses < 0:
                print("\nNumber of courses cannot be negative")
            else:
                break
        StdManagement.num_of_courses = num_of_courses

def getStudentInfo():
        while True:
            student_id = input("\nEnter student ID: ")
            if student_id is None:
                print("Student ID cannot be null!")
            else:
                break
        if student_id in StdManagement.std_id_list:
            print("Student ID already exists!")
            exit()
        else:
            while True:
                name = str(input("Enter student name: "))
                if name is None:
                    print("Student name cannot be null!")
                else:
                    break
            while True:
                dob = input("Enter student dob/ date of birth: ")
                if dob is None:
                    print("Student dob/ date of birth cannot be null!")
                else:
                    break
            print(f"Added student {name}!")
            InitStudent(StdManagement, student_id, name, dob)

def getCourseInfo():
        while True:
            course_id = input("\nEnter course ID: ")
            if course_id is None:
                print("Course ID cannot be null!")
            else:
                break
        if course_id in StdManagement.courses_id_list:
            print("Course ID already exists!")
            exit()
        else:
            name = input("Enter course name: ")
            if name is None:
                print("Course name cannot be null!")
            while True:
                credit = int(input("Enter course credits: "))
                if credit < 0:
                    print("Number of credits can not be negative!")
                elif credit is None:
                    print("Course credits cannot be null!")
                else:
                    break
            print(f"Added course {name}!")
            InitCourse(StdManagement, course_id, name, credit)

def getCourseMark(course_id):
        for student in StdManagement.std_info_list:
            student_id = student.getStudentID()
            studentName = student.getName()
            m = math.floor(float(input(f"Enter marks for {studentName}: ")))
            InitMark(StdManagement, student_id, course_id, m)

def getMark():
        while True:   
            course_id = input("Enter the course ID for which you want to input marks: ")
            if course_id in StdManagement.courses_id_list:
                if len(StdManagement.marks_list) > 0:
                    Marked = False
                    for mark in StdManagement.marks_list:
                        if mark.getCourseID() == course_id:
                            print("You have already input marks for this course!")
                            Marked = True
                            break
                    if not Marked:
                        getCourseMark(course_id)
                else:
                    getCourseMark(course_id)
                break
            elif course_id is None:
                print("Course ID cannot be null!")
            else:
                print("No course with such ID!")
                return False