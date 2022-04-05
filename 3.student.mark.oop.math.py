import math
import numpy as np

class InitStudent:
    def __init__(self, StdManagment, student_id, name, date_of_birth):
        self.stdID = student_id
        self.stdName = name
        self.dob = date_of_birth
        StdManagment.std_info_list.append(self)
        StdManagment.std_id_list.append(self.stdID)

    def getStudentID(self):
        return self.stdID

    def getName(self):
        return self.stdName

    def getDOB(self):
        return self.dob

    def setGPA(self, gpa):
        self.gpa = gpa

    def getGPA(self):
        return self.gpa

class InitCourse:
    def __init__(self, StdManagment, course_id, name, credit):
        self.courseID = course_id
        self.stdName = name
        self.credit = credit
        StdManagment.courses_list.append(self)
        StdManagment.courses_id_list.append(self.courseID)

    def getCourseID(self):
        return self.courseID

    def getName(self):
        return self.stdName

    def getCredit(self):
        return  self.credit

class InitMark:
    def __init__(self, StdManagment, student_id, course_id, student_mark):
        self.stdID = student_id
        self.courseID = course_id
        self.stdMark = student_mark
        StdManagment.marks_list.append(self)

    def getStudentID(self):
        return self.stdID

    def getCourseID(self):
        return self.courseID

    def getStudentMark(self):
        return self.stdMark

class StdManagement:

    std_id_list = []
    std_info_list = []
    courses_list = []
    courses_id_list = []
    marks_list = []
    number_std = None
    num_of_courses = None

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
                    print("Course credit cannot be null!")
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

def menu():
        print("1. Set information of student: \n"
          "2. Set information of course: \n"
          "3. Set mark for student by course:\n"
          "4. Get information of student: \n"
          "5. Get information of course: \n"
          "6. Print Mark:\n"
          "7. Compute Gpa:\n"
          "8. Sort List:\n"
          "0. Quit!!")
        option = int(input("Enter your choice: "))
        return option    

while True:
    print("\n================================================") 
    option = menu()
    if option == 1:
        getNumOfStudents()
        for i in range(StdManagement.number_std):
            print(f"Student #{i + 1}:\n")
            getStudentInfo()
    elif option == 2:
        getNumOfCourses()
        for i in range(StdManagement.num_of_courses):
            print(f"Course #{i + 1}:")
            getCourseInfo()
    elif option == 3:
        getMark()
    elif option == 4:
        printStudents()
    elif option == 5:
        printCourses()
    elif option == 6:
        printMarks()
    elif option == 7:
        PrintGPA()
    elif option == 8:
        printSortedList()
    else:
        print("Quit")
        break


