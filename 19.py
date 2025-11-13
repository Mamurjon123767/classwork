class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    def is_passing(self):
        if self.grade >= 50:
            print("Pass")
        else:
            print("Fail")
student1 = Student("Mamurjon", 82)
student1.is_passing()
