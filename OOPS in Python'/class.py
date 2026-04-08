'''class student:
    def __init__(self,name,marks,attendance):
        self.name=name
        self.marks=marks
        self.attendance=attendance
    def display(self):
        print("Name:",self.name)
        print("Marks:",self.marks)
        print("Attendance:",self.attendance)


s1=student("Ram",85,90)
s1.display()
s2=student("Shyam",90,95)
s2.display()

    def calculate_grade(self):
         if self.marks>=90:
            return "A"
         elif self.marks>=80:
            return "B"
         elif self.marks>=70:
             return "C"
         elif self.marks>=60:
            return "D"
         else:
            return "F"
        
s1=student("Ram",85,90)
s1.display()
print("Grade:", s1.calculate_grade())
'''


class student:
    def __init__(self, name, marks, attendance):
        self.name = name
        self.marks = marks
        self.attendance = attendance

    def calculate_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 80:
            return "B"
        elif self.marks >= 70:
            return "C"
        else:
            return "F"

s1 = student("Ram", 85, 90)
print("Name:", s1.name)
print("Marks:", s1.marks)
print("Attendance:", s1.attendance)
print("Grade:", s1.calculate_grade())