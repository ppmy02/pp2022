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