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