class Student():
    def __init__(self, name, major, cgpa):
        self.name = name
        self.major = major
        self.cgpa = cgpa
        

    def on_scholarship(self):
        if self.cgpa >= 8.5:
            return True
        else:
            return False
   
students_data = [("Amit", "CS", 8.4), 
            ("T", "Bcom", 8.9)
            ]

students = [Student(name, major, cgpa) for name, major, cgpa in students_data]

for student in students:
    print(f"{student.name} on scholarship : {student.on_scholarship()}")
    

'''class Student():
    def __init__(self, name, major, cgpa):
        self.name = name
        self.major = major
        self.cgpa = cgpa
        

    def on_scholarship(self):
        if self.cgpa >= 8.5:
            return True
        else:
            return False
   
student1 = Student("Amit", "CS", 8.4)
student2 = Student("T", "Bcom", 8.9)

print(student2.on_scholarship())
'''

