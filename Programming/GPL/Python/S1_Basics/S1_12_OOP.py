
#   OOP

#T# OOP stands for Object Oriented Programming

#T# Contents
#T# Parts of a class
#T# Attributes

#T# class statement
class ClassName1:
    "here goes the class docstring"

#T# class var shared by all instances
    classVar1 = 7

#T# constructor method with __init__
    def __init__(self,attr1,attr2):
        self.attr1 = attr1
        self.attr2 = attr2

#T# destructor method with __del__
    def __del__(self):
        print("destroying object with",self.__dict__)
    
    def getAttr1(self):
        return self.attr1

    def setAttr1(self,nAttr1):
        self.attr1 = nAttr1

#T# make an instance of a class calling the constructor
obj1 = ClassName1(5,"str1")

#T# call methods from the class through the object
print("The attribute one is:",obj1.getAttr1())

#T# access a class variable through the class
print("Class variable is:",ClassName1.classVar1)

#T# Parts of a class

#T# import the inspect module to get the parts of a class
import inspect

#T# get the members of a class, this returns methods, attributes
inspect.getmembers(obj1)

#T# Attributes

#T# access attributes directly through the object
print("Attribute 2 is",obj1.attr2)

#T# built-in class attributes
#T# the __dict__ attribute contains
print("The object's namespace is:",obj1.__dict__)
print("The class' docstring is:",obj1.__doc__)
print("The class' name is:",ClassName1.__name__)
print("The class' module is:",obj1.__module__)
print("The base classes are:",ClassName1.__bases__)

#T# class inheritance
class DerivedClass1 (ClassName1):
    def childMethod1(self):
        print("Called the child's method")

#T# override parent's methods
    def setAttr1(self):
        print("Sorry, this method has been overridden")

#T# string representations __repr__, __str__
    def __repr__(self):
        return "Representation of the object"
    def __str__(self):
        return "String of the object"

#T# class' hidden variables with __varN
    __hiddenVar1 = 9

#T# access hidden variable inside class
    def hidAccess(self):
        self.__hiddenVar1 *= 2
        return self.__hiddenVar1

objCh1 = DerivedClass1("strCh1","strCh2")
objCh1.childMethod1()
print("Child object's attribute one:",objCh1.getAttr1())

#T# know if a class is a subclass of another with issubclass()
print("is DerivedClass1 a subclass of ClassName1?",\
issubclass(DerivedClass1,ClassName1))

#T# know if an object is an instance of a class with isinstance()
print("is obj1 an object of ClassName1?",isinstance(obj1,ClassName1))

#T# call overridden method
objCh1.setAttr1()

#T# original __repr__, __str__
print(repr(obj1))
print(str(obj1))

#T# derived __repr__, __str__
print(repr(objCh1))
print(str(objCh1))

#T# access hidden variable from outside class with _ClassName__hidVarName
print("Current hidden variable:",objCh1._DerivedClass1__hiddenVar1)
print("Returned from hidden variable:",objCh1.hidAccess())