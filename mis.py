class Person:
    def __init__(self, firstname,lastname,age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
    
class Student(Person):
    def __init__(self, firstname, lastname, age,hall,courses=None):
        super().__init__(firstname, lastname, age)
        if courses is None:
            self.courses = []
        else:
            self.courses = courses
        self.hall = hall
    
    def add_course(self,course):
        self.courses.append(course)

    def drop_course(self,course):
        self.courses.remove(course)

    def print_all_courses(self):
        for course in self.courses:
            print(course)



me = Student('huby','lex',23,'nelson')
me.add_course('math')
me.add_course('english')
me.print_all_courses()
