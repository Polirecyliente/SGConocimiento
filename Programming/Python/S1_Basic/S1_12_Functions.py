#!/usr/bin/python3
#   Functions

#T# def funName (param1,param2 = defaultV,*paramTuple): "docstring" return
def fun1 (f1arg1,f1arg2 = 8,*f1argTuple):
    "here goes the fun1 docstring or documentation string with its purpose"
    f1arg1 = f1arg1 * (2 + f1arg2)
    varF1 = f1arg1
    for varTup in f1argTuple:
        print(varTup)
    return varF1

#T# get the docstring of a function with fun1.__doc__
print("fun1() docstring:",fun1.__doc__)

f1arg1 = 6
#T# function call funName(param1 = keywordArg)
ret1 = fun1(f1arg1 = f1arg1)
print("val of arg",f1arg1,"\nval of ret",ret1)

#T# call a function with an argument that unpacks a list or tuple (*param)
fun1(1,8,"3tuple","z8","str1")

#T# define a function with an unpackable dictionary with the ** operator
def funKWunpack(**paramDict):
    for varKey in paramDict:
        print(paramDict[varKey])

#T# call a function with an argument that unpacks a dictionary (**dict), this can be used as a dictionary of keyword arguments
dict1 = {'k1':"val1",'key2':"value2"}
funKWunpack(**dict1)

#T# return multiple values from a function by using a tuple, list, or dict
def retMultiValsInTuple():
    return(3,'st0')

#T# assing multiple values from a tuple
va1, va2 = retMultiValsInTuple()
print("va1 is:",va1,"va2 is:",va2)

#T# anonymous function with lambda
opFun1 = lambda aFarg1,aFarg2: 7 * aFarg1 + (aFarg2 - 1)
valOp1 = opFun1(3,4)
print("after anonymous function",valOp1)