class School:
    def __init__(self):
        self.students = []
    def add_student(self, name):
        self.students.append(name)
    def show_students(self):
        for name in self.students:
            print(name)
s = School()
s.add_student("Mamurjon")
s.add_student("John")
s.show_students()
