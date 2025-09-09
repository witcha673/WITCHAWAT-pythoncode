
    # สร้าง class Student โดยกำหนดให้
    # - มี attribute ชื่อ name, age, และ student_id ที่เก็บข้อมูลทั่วไปของนักเรียน และ grades ที่เก็บคะแนนของนักเรียนในแต่ละวิชา โดยเป็นโครงสร้างข้อมูลประเภท list
    # - มี method ชื่อ add_grade(subject, grade) โดย grade เป็น dictionary ที่เก็บคะแนนของนักเรียนในแต่ละวิชา
    #     { 
    #         "subject": "Mathematics", "grade": 85 
    #     }
    # - มี method ชื่อ get_average_grade() ที่คืนค่าเฉลี่ยคะแนนของนักเรียน
    # - มี method ชื่อ get_grade_report() ที่คืนค่ารายงานผลการเรียนของนักเรียน

class Student:
    def __init__(self,name,age,student_id):
        self.name = name
        self.age = age
        self.student_id = student_id
        self.grades = []
    def add_grade(self,subject,grade):
        self.grades.append({"subject": subject, "grade": grade})

    def get_avarage_grade(self):
        if not self.grades:
            return 0
        total = sum(grade["grade"] for grade in self.grades)
        return total / len(self.grades)
    def get_grade_report(self):
        report = f"Grade Report for {self.name} (ID: {self.student_id}):\n"
        for grade in self.grades:
            report += f"{grade['subject']}: {grade['grade']}\n"
        report += f"Average Grade: {self.get_avarage_grade():.2f}"
        return report
    
student1 = Student("Alice",20,"12345")
student1.add_grade("Mathematics",85)
student1.add_grade("Science",90)
student1.add_grade("History",78)
print(student1.get_grade_report())






    # สร้าง class Rectangle โดยกำหนดให้
    # - มี attribute ชื่อ length และ width ที่เก็บข้อมูลความยาวและความกว้างของสี่เหลี่ยม
    # - มี method ชื่อ get_area() ที่คืนค่าพื้นที่ของสี่เหลี่ยม
    # - มี method ชื่อ get_perimeter() ที่คืนค่ารอบรูปของสี่เหลี่ยม

class Rectangle:
        def __init__(self,lenght,width):
            self.lenght = lenght
            self.width = width
        def get_area(self):
            return self.lenght * self.width
        def get_perimeter(self):
            return 2 * (self.lenght + self.width)
    
Rectangle1 = Rectangle(5,10)
print("Area:",Rectangle1.get_area())



