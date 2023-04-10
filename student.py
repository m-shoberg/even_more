class Student:
    def __init__(self, last, first, grade):
        self.last = last
        self.first = first
        self.grade = grade
        self.standard_name_line = first + ' ' + last + ' ' + grade

    def fullname(self):
        return('{} {}'.format(self.first, self.last))
    
student_1 = Student('Shoberg', 'Marcus', 'Sophmore')
student_2 = Student('Schwarz', 'Andrew', 'Junior')
student_3 = Student('Shoemaker', 'Shane', 'Freshman')
student_4 = Student('Bill', 'Wesley', 'Senior')

print(student_1.standard_name_line)
print(student_2.standard_name_line)
print(student_3.standard_name_line)
print(student_4.standard_name_line)

print(student_1.fullname())


class Circle:
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color
        
    def double_radius(self):
        return('{}'.format(self.radius * 2))

circ_1 = Circle(3, 'Blue')
circ_2 = Circle(12, 'Purple')
circ_3 = Circle(5, 'Green')
circ_4 = Circle(7, 'Yellow')

print(circ_1.double_radius())

