#Build a student class

class Student:
    
    def __init__(self, first, last, courses=None):
        self.first = first
        self.last = last
        if courses == None:
            self.courses = []
        else:
            self.courses = courses
            
    def __str__(self) -> str:
        return f'{self.first} {self.last} is in {self.courses}'
    
    
    def add_course(self, course):
        if course not in self.courses:
            self.courses.append(course)
        else:
            print(f'{self.first} is already enrolled in the {course} course.')
            
    
    def remove_course(self, course):
        if course in self.courses:
            self.courses.remove(course)
        else:
            print(f"{course} not found in {self.first}'s courses.")
        

course1 = ["python", "rails", "javascript"]
course2 = ['java', 'rails', 'c']


s1 = Student("Gino", "De Paoli",course1)
s2 = Student('Mia', 'De Paoli', course2)

# print(s1.first, s1.last, s1.courses)
# print(s2.first, s2.last, s2.courses)
print(s1)
print(s2)


s1.add_course('java')
s1.add_course('rails')
# print(s1.first, s1.last, s1.courses)

s2.remove_course('c')
s2.remove_course('c')
s2.remove_course('python')
# print(s2.first, s2.last, s2.courses)