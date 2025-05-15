class People:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def get_email(self):
        return f"{self.firstname.lower()}.{self.lastname.lower()}.uni@btu.edu.ge"


class Lecturer(People):
    def __init__(self, firstname, lastname, salary):
        super().__init__(firstname, lastname)
        self.salary = salary

    def get_email(self):
        return f"{self.firstname.lower()}.{self.lastname.lower()}@btu.edu.ge"


class Student(People):
    def __init__(self, firstname, lastname, courses=None):
        super().__init__(firstname, lastname)
        self.courses = courses if courses is not None else []

    def get_email(self):
        return f"{self.firstname.lower()}.{self.lastname.lower()}.1@btu.edu.ge"



lecturer = Lecturer("saba", "artkmeladze", 5000)
student = Student("juja", "juja", ["Math", "Physics"])
people = People("luka", "megrelishvili")
print(lecturer.get_email())
print(student.get_email())
print(people.get_email())