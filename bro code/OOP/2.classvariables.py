# class variables =  Shared among all instances (objects) of a class
#                    Defined outside the constructor
#                    Allow you to share data among all objects created from that class

class Student:

   # class variables
   class_year = 2025
   num_students = 0

   def __init__(self, name, age):
       # self refers to the object we currently working with
       self.name = name
       self.age = age
       # using a class variable
       Student.num_students += 1

student1 = Student("Spongebob", 30)
print(Student.num_students)
student2 = Student("Patrick", 35)
print(Student.num_students)
student3 = Student("Squidward", 55)
print(Student.num_students)
student4 = Student("Sandy", 27)
print(Student.num_students)

print(f"{student1.name} , {student2.age} his class year is {student1.class_year} " )
print()

print(f"My graduating class of {Student.class_year} has {Student.num_students} students")
print()
print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)