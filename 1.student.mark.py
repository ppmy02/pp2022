
    # arrays containing info
students_id_list = []
students_info_list = []
courses_list = []
courses_id_list = []
marks = []

def NumOfStds():
    while True:
        num_of_students = int(input("Total number of students: "))
        if (num_of_students < 0):
            print("Negative number of students is not valid!")
        else:
            break
    return num_of_students

# dictionary for student infomation
def CreateStudentDict(student_id, name, dob):
    aboutStudent = {
        "id": student_id,
        "name": name,
        "dob": dob
    }
    students_info_list.append(aboutStudent)
    students_id_list.append(student_id)

def NumOfCourses():
    while True:
        num_of_courses = int(input("Total number of courses: "))
        if num_of_courses < 0:
            print("Negative number of courses is not valid")
        else:
            break
    return num_of_courses

    # create a dictionary for course infomation
def CreateCourseDict(course_id, name):
    aboutCourse = {
        "id": course_id,
        "name": name
    }
    courses_list.append(aboutCourse)
    courses_id_list.append(course_id)

    # create a dictionary for the marks
def CreateMarkDict(student_id, course_id, value):
    aboutMark = {
        "sid": student_id,
        "cid": course_id,
        "value": value
    }
    marks.append(aboutMark)

def StudentInfoQuery():
    while True:
        sid = input("Enter student ID: ")
        if len(sid) == 0 or sid is None:
            print("Negative student ID is not allowed!")
        else:
            break
    if sid in students_id_list:
        print("Student ID already exists")
        exit()
    else:
        while True:
            name = input("Enter student name: ")
            if len(name) == 0 or name is None:
                print("Student name cannot be empty!")
            else:
                break
        while True:
            dob = input("Enter student date of birth: ")
            if len(dob) == 0 or dob is None:
                print("Student date of birth cannot be empty!")
            else:
                break
        print(f"Student {name} successfully added!")
        CreateStudentDict(sid, name, dob)

def GetCourseInfo():
    while True:
        cid = input("Enter course ID: ")
        if len(cid) == 0 or cid is None:
            print("Course ID cannot be empty!")
        else:
            break
    if cid in courses_id_list:
        print("Course ID already exists!")
        exit()
    else:
        while True:
            name = input("Enter course name: ")
            if len(name) == 0 or name is None:
                print("Course name cannot be empty")
            else:
                break
        print(f"Successfully added course: {name}")
        CreateCourseDict(cid, name)

def GetCourseMarks(cid):
    if not students_info_list:
        print("There 0 student in the course Pls input Student!")
    else:
        for s in students_info_list:
            sid = s['id']
            while True:
                value = float(input(f"Enter marks for student {s['name']}: "))
                if value < 0:
                    print("Marks must be non-negative")
                else:
                    break
            CreateMarkDict(sid, cid, value)


def GetMarks():
    if not courses_list:
        print("You have 0 course now Pls Input Course First")
    else:
        while True:
            cid = input("Enter Course ID for which you want to input marks: ")
            if cid in courses_id_list:
                if len(marks) > 0:
                    marked = False
                    for m in marks:
                        if m['cid'] == cid:
                            print("You have already input marks for this course")
                            marked = True
                            break
                    if not marked:
                        GetCourseMarks(cid)
                else:
                    GetCourseMarks(cid)
                break
            elif len(cid) == 0 or cid is None:
                print("Course ID cannot be empty!")
            else:
                print("No course found for the input ID")
                return -1


def PrintCourses():
    if not courses_list:
        print("List is empty!")
    else:
        print("List of all Courses:")
        for c in courses_list:
            print("%s %s" % (c['id'], c['name']))

        print()


def PrintStudents():
    if not students_info_list:
        print("List is empty!")
    else:
        print("All Students in class:")
        for s in students_info_list:
            print("%s | %s | %s" % (s['id'], s['name'], s['dob']))

        print()

def PrintCourseMarks(cid):
    for m in marks:
        if m['cid'] == cid:
            sid = m['sid']
            for s in students_info_list:
                if s['id'] == sid:
                    print("%s | %s | %s" % (s['id'], s['name'], m['value']))

def PrintMarks():
    if not courses_list:
        print("You have 0 course now Pls Input Course")
    else:
        while True:
            cid = input("Enter the course ID for which you want to see marks: ")
            if len(cid) == 0 or cid is None:
                print("Course ID cannot be empty!")
            else:
                break
        if cid in courses_id_list:
            PrintCourseMarks(cid)
        else:
            print("No course exists for the input ID")
            return -1

def options():
    print("""
    Choose?
    1. Input students' info
    2. Input courses' info
    3. Input mark for a course
    4. List student
    5. List course
    6. Print marks of a course
    7. Exit
    """)
    option = int(input())
    return option
def main():
    print("What now?")
    while True:
        option = options()
        if option == 1:
            num_of_stds = NumOfStds()
            for i in range(num_of_stds):
                print(f"-Student {i + 1}-")
                StudentInfoQuery()
        elif option == 2:
                num_of_courses = NumOfCourses()
                for i in range(num_of_courses):
                        print(f"Course {i + 1}:")
                        GetCourseInfo()
        elif option == 3:
            GetMarks()
        elif option == 4:
            PrintStudents()
        elif option == 5:
            PrintCourses()
        elif option == 6:
            PrintMarks()
        elif option == 7:
            break
        else:
            break   
main()