class Person:
    # Constructor
    def __init__(self, name,age):
        self.__name= name
        self.__age= age
    def get_person(self):
        print("Name: ",name)
        print("Age: ",age)
# Inherited or Subclass
class Student(Person):
    def __init__(self, sid,sem,sub1,sub2):
        super().__init__(name,age)
        self.__sid= sid
        self.__sem= sem
        self.__sub1=sub1
        self.__sub2=sub2
    def get_student(self):
        print("ID: ",sid)
        print("Semester: ",sem)
        print("Subject 1 marks: ",sub1)
        print("Subject 2 marks: ",sub2)
    def calculation(self):
        avg=(sub1+sub2)/2.0
        print("Average Marks: ",avg)
# Testing class capability
print("Enter your Name,Age,ID,Semester and Marks of two subjects")
name=input()
age=int(input())
p= Person(name,age)
sid=int(input())
sem=int(input())
sub1=int(input())
sub2=int(input())
s=Student(sid,sem,sub1,sub2)
p.get_person()
s.get_student()
s.calculation()
