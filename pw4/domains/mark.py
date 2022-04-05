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