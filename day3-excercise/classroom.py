#################################################
#  File Name:person.py
#  Author: Pengwei.Xing
#  Mail: xingwei421@qq.com,pengwei.xing@igp.uu.se,xpw1992@gmail.com
#  Created Time: Wed Mar  8 13:11:02 2023
#################################################

class Person:
    def __init__(self,first,last):
        self.first = first
        self.last = last

    def printFullname(self):
        print("%s\t%s" %(self.last,self.first))


class Student(Person):
    def __init__(self,first,last,subject):
        Person.__init__(self,first,last)
        self.subject = subject
    def printNameSubject(self):
        print(self.last,self.first,self.subject)

class Teacher(Person):
    def __init__(self,first,last,course):
        Person.__init__(self,first,last)
        self.course  = course
    def printNameCourse(self):
        print(self.last,self.first,self.course)
