import math
import numpy as np
from domains.StdManagement import *

def printCourses():
        print("Printing all courses: ")
        for course in StdManagement.courses_list:
            print("ID = %s, %s" % (course.getCourseID(), course.getName()))
            
def printStudents():
        print("Printing all Students in class:")
        
        for student in StdManagement.std_info_list:
            print("%s %s %s" % (student.getStudentID(), student.getName(), student.getDOB()))
            
def printCourseMarks(course_id):
        for mark in StdManagement.marks_list:
            if mark.getCourseID() == course_id:
                student_id = mark.getStudentID()
                for student in StdManagement.std_info_list:
                    if student.getStudentID() == student_id:
                        print(f"%s %s %s" % (student.getStudentID(), student.getName(), mark.getStudentMark()))
            
def printMarks():
        while True:      
            course_id = input("Enter the course ID for which you want to list marks: ")
            if course_id is None:
                print("Course ID cannot be null")
            else:
                break
        if course_id in StdManagement.courses_id_list:
            printCourseMarks(course_id)
        else:
            print("There exist no course with that ID!")
            return False

def computeGPA(sid):
        marks_arr = np.array([])
        course_credits = np.array([])
        for mark in StdManagement.marks_list:
            if mark.getStudentID() == sid:
                for course in StdManagement.courses_list:
                    if course.getCourseID() == mark.getCourseID():
                        marks_arr = np.append(marks_arr, mark.getStudentMark())
                        course_credits = np.append(course_credits, course.getCredit())
        gpa = np.dot(marks_arr, course_credits) / np.sum(course_credits)
        rounded_gpa = math.floor(gpa)

        for student in StdManagement.std_info_list:
            if student.getStudentID() == sid:
                student.setGPA(rounded_gpa)

def PrintGPA():
        while True:
            sid = input("Enter student ID to compute the student GPA: ")
            if len(sid) == 0 or sid is None:
                print("Student ID cannot be null!")
            elif sid not in StdManagement.std_id_list:
                print("Student ID does not exist!")
            else:
                break
        for student in StdManagement.std_info_list:
            if student.getStudentID() == sid:
                computeGPA(sid)
                print("Student %s has GPA = %.1f" % (student.getName(), student.getGPA()))
                
                break

def printSortedList():

        new_student_list = []
        for student in StdManagement.std_info_list:
            computeGPA(student.getStudentID())
            new_student = (student.getStudentID(), student.getName(), student.getGPA())
            new_student_list.append(new_student)
            
        dtype = [('sid', 'S10'), ('name', 'S30'), ('gpa', float)]
        numpy_student_list = np.array(new_student_list, dtype=dtype)
        sorted_student_list = np.sort(numpy_student_list, order='gpa')[::-1]

        new_sorted_student_list = []
        for student in sorted_student_list:
            decoded_student = (student[0].decode(), student[1].decode(), student[2])
            new_sorted_student_list.append(decoded_student)
        for student in new_sorted_student_list:
            print("ID = %s, %s, GPA = %s\n" % (student[0], student[1], student[2]))