
#   OOP

#T# Table of contents

#C# Class definition
#C# - Hidden variables
#C# Instantiation
#C# Parts of a class
#C# - Attributes
#C# - Methods
#C# - Class variables
#C# - Hidden variables
#C# - General parts
#C# Inheritance
#C# - Multiple inheritance
#C# - Method Resolution Order (MRO)

#T# Beginning of content

# |-------------------------------------------------------------
#T# OOP stands for Object Oriented Programming
# |-------------------------------------------------------------

#C# Class definition

# |-------------------------------------------------------------
#T# the class keyword is used to define the classes

# SYNTAX class definition
# class Class_name1:
#     "class_docstring1"
#     class_attribute1 = val1
#     def class_method1(self, params):
#         statements1
#T# the class name is Class_name1, the docstring is "class_docstring1", inside the class, attributes and methods can be defined, such as class_attribute1, and class_method1

#T# in the class methods, the self keyword is the first parameter, it allows methods to access the calling instance 

class Class_name1:
    "here the class docstring"

#T# a class attribute is a variable shared by all instances, it's defined outside all methods
    class_attr1 = 1

#T# the self keyword is used to represent the calling instance, given an instance obj1, the expression obj1.method1() is shorthand for Class_name1.method1(obj1), obj1 being in the self keyword place, the first parameter of method1

#T# the constructor method is called __init__
    def __init__(self, attr1_param, attr2_param):

#T# instance attributes are defined after the self keyword
        self.attr1 = attr1_param
        self.attr2 = attr2_param

#T# the destructor method is called __del__, it's called when an instance goes out of scope
    def __del__(self):
        Class_name1.class_attr1 += 1

#T# class methods are defined as normal functions
    def get_attr1(self):
        return self.attr1

    def set_attr1(self, new_attr1):
        self.attr1 = new_attr1

#C# - Hidden variables

# |-----
#T# creating hidden variables
# SYNTAX __hidden_var_name1 = val1
#T# the name of a hidden variable starts with double underscore
    __hidden1 = 9

#T# access a hidden variable inside the class as a normal attribute
    def get_hidden_var1(self):
        self.__hidden1 *= 2
        return self.__hidden1
# |-----

# |-------------------------------------------------------------

#C# Instantiation

# |-------------------------------------------------------------
#T# make an instance of a class by calling the constructor
obj1 = Class_name1(5, "str1")

#T# objects in local scope can be made by instantiating them inside a function
def func1():
    local_obj1 = Class_name1(1, "2")
    return None

#T# the destructor is called when the local instances go out of scope
func1()
func1()
# Class_name1.class_attr1 == 3
# |-------------------------------------------------------------

#C# Parts of a class

# |-------------------------------------------------------------

#C# - Attributes

# |-----
#T# access attributes directly through the object with dot notation
str1 = obj1.attr2 # str1
# |-----

#C# - Methods

# |-----
#T# call methods from the class through the object with dot notation
int1 = obj1.get_attr1() # 5
# |-----

#C# - Class variables

# |-----
#T# access a class variable through the class with dot notation
int1 = 2 * Class_name1.class_attr1 # 6
# |-----

#C# - Hidden variables

# |-----
#T# access hidden variables from outside the class

# SYNTAX var1 = obj1._Class1__hidden_var_name1
#T# the hidden variable is accessed as an attribute of obj1, it must be written as, an underscore, the class name, two underscores, the variable name

int1 = obj1._Class_name1__hidden1 # 9
# |-----

#C# - General parts

# |-----
#T# import the inspect module to get the parts of a class
import inspect

#T# the getmembers function returns the members of a class, which are methods, attributes
list1 = inspect.getmembers(obj1) # long list

#T# the __dict__ attribute is a dictionary with the members and their values from classes and instances
dict1 = Class_name1.__dict__ # {'__module__': '__main__', '__doc__': 'here the class docstring', 'class_attr1': 3, '__init__': <function Class_name1.__init__ at 0x7f4abc05dca0>, '__del__': <function Class_name1.__del__ at 0x7f4abc05df70>, 'get_attr1': <function Class_name1.get_attr1 at 0x7f4abc06d040>, 'set_attr1': <function Class_name1.set_attr1 at 0x7f4abc06d0d0>, '__dict__': <attribute '__dict__' of 'Class_name1' objects>, '__weakref__': <attribute '__weakref__' of 'Class_name1' objects>}
dict1 = obj1.__dict__ # {'attr1': 5, 'attr2': 'str1'}

#T# the __doc__ attribute contains the docstring
str1 = Class_name1.__doc__ # here the class docstring <class 'str'>
str1 = obj1.__doc__        # here the class docstring <class 'str'>

#T# the __name__ attribute contains the name of the class
str1 = Class_name1.__name__ # Class_name1

#T# the __module__ attribute contains the module of the class, or instance
str1 = Class_name1.__module__ # __main__
str1 = obj1.__module__ # __main__

#T# the __bases__ attribute
tuple1 = Class_name1.__bases__ # (<class 'object'>,)
# |-----

# |-------------------------------------------------------------

#C# Inheritance

# |-------------------------------------------------------------
#T# classes can inherit from preexisting classes

# SYNTAX class inheritance
# class Derived_class1 (Parent_class1):
#     def parent_method1(self, params)
#         statements1
#     def child_new_method1(self, params):
#         statements2
#T# to inherit, the parent class must go in parentheses after the class name, and the parent methods like parent_method1 can be overridden

class Derived_class1 (Class_name1):

#T# create child instance attributes and inherit the parent ones in the constructor
    def __init__(self, attr1_param, attr2_param, new_attr_param):

# |--------------------------------------------------\
#T# the super function returns an object of the parent class

# SYNTAX super().parent_method1(args)
#T# the parent's methods and attributes can be accessed through this object

        super().__init__(3 * attr1_param, attr2_param)
# |--------------------------------------------------/

        self.new_attr1 = new_attr_param
        self.new_attr2 = 888

    def child_new_method1(self):
        return 35

#T# override a parent method
    def set_attr1(self):
        self.attr1 = self.attr1 - 1

#T# the __repr__, and __str__ functions can be overridden, the change will be seen when calling the repr and str functions respectively
    def __repr__(self):
        return "Representation of the object"
    def __str__(self):
        return "String of the object"

#T# a child object is instantiated the same way as the parent
child_obj1 = Derived_class1(4, "child_str", "child_new_str")

#T# the following examples show a few of the child methods, and attributes
int1 = child_obj1.child_new_method1() # 35
int1 = child_obj1.get_attr1() # 12 == 4 * 3
int1 = child_obj1.new_attr2 # 888

#T# original __repr__, __str__
str1 = repr(obj1)       # <__main__.Class_name1 object at 0x7feebbae2a30>
str1 = str(obj1)        # <__main__.Class_name1 object at 0x7feebbae2a30>

#T# derived __repr__, __str__
str1 = repr(child_obj1) # Representation of the object
str1 = str(child_obj1)  # String of the object

#C# - Multiple inheritance

# |-----
#T# for multiple inheritance, at least two parent classes are required

# SYNTAX multiple inheritance
# class Derived_class1 (Parent_class1, Parent_class2):
#     class_statements1
#T# the parent classes are written inside parentheses separated by comma

class Derived_class2 (Class_name1):
    def set_attr1(self):
        self.attr1 = 2 * self.attr1

class Multiple_parents_class1 (Derived_class2, Derived_class1):
    pass

#T# normal instantiation, and access in multiple inheritance
multi_parent_obj1 = Multiple_parents_class1(5, "multi_parent", "s")
int1 = multi_parent_obj1.attr1 # 15
# |-----

#C# - Method Resolution Order (MRO)

# |-----
#T# the MRO is used to decide which of the parents methods to use when several parents have the same method, the MRO allows to select which of the methods to inherit

#T# the first inherited class has priority in the MRO
multi_parent_obj1.set_attr1()
int1 = multi_parent_obj1.attr1 # 30, here the Derived_class2 method was used because this class is first in the parentheses of parent classes from the Multiple_parents_class1

#T# it's possible to call one of the methods that wasn't inherited

# SYNTAX Parent_class1.method1(child_obj1)
#T# this calls the method1 from the parent Parent_class1, even if it wasn't inherited by the child class

Derived_class1.set_attr1(multi_parent_obj1)
int1 = multi_parent_obj1.attr1 # 29

#T# the mro function returns a list of the classes in order, in which a member will be searched for, or the same as the order of the classes inherited, the class 'object' is the base class of all classes
list1 = Multiple_parents_class1.mro() # [<class '__main__.Multiple_parents_class1'>, <class '__main__.Derived_class2'>, <class '__main__.Derived_class1'>, <class '__main__.Class_name1'>, <class 'object'>]
# |-----

# |-------------------------------------------------------------