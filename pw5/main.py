import os
import zipfile
from input import *
from output import *

def menu():
        if os.path.isfile("students.dat"):
            zip_file = zipfile.ZipFile("students.dat", "r")
            zip_file.extractall()
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
    if os.path.isfile("students.dat"):
        zip_file = zipfile.ZipFile("students.dat", "r")
        zip_file.extractall()
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
        print("GoodBye!")
        file_list = ["students.txt", "courses.txt", "marks.txt"]
        with zipfile.ZipFile("students.dat", "w") as new_zip:
            for file_name in file_list:
                new_zip.write(file_name)
        os.remove("students.txt")
        os.remove("courses.txt")
        os.remove("marks.txt")
        break
