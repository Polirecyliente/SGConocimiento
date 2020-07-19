
#   Data types

#T# multiple variable assignment
#T# integer, double, string
int1 = int2 = 5; dou1 = dou2 = 12.415; str1 = str2 = "stringsVl"
int1 = 2
int3,int4 = 72,12

#T# delete statement
del int3,int4

#T# numerical types are long, float, complex j, octal 0o, hexa 0x
lon1 = 0x17 - 0o11
flo1 = 64.51E2
complex1 = 5.1 + 3.28j

#T# strings, slice operator [:], concat operator +, repetition operator *
str3 = str1[0]
#T# in [iniEl:finalEl] include iniEl, up to before finalEl (exclude finalEl)
str4 = str1[2:5]
#T# in [iniEl:finalEl:stepN] include iniEl and step by stepN elements
str4a = str1[2:8:3]
str5 = str1 * 2 + "|" + str2

#T# arrays [] aka lists
arr1 = [3,5,2,-1]

#T# lists [], slice operator [:], concat operator +, repetition operator *
list1 = [1,2,"subS1",9,"S2"]
subL1 = list1[0]
subL2 = list1[1:3]
subL3 = list1[4:5] * 4 + subL2

#T# tuples (): read-only lists
tupl1 = (1,2,"subS1",9,"S2")
#T# next example gives error: tupl1[0] = 3
subT1 = tupl1[0]
subT2 = tupl1[1:3]
subT3 = tupl1[3:4] * 3 + subT2

#T# tuples can be created without parentheses
tupl3 = 1,6, 5,
print("tupl3 is:",tupl3)

#T# dictionaries {}: python's hash table with key value pairs
dict1 = {'Fis':63.2,'Sec':12.1,'Thd':9.8}
dict1['Thd'] = 19.8
dict1keys = dict1.keys()
dict1vals = dict1.values()

#T# data type conversion: int(), float(), complex(), str(), repr(), eval(), tuple(), list(), set(), dict(), frozenset(), chr(), ord(), hex(), oct()
str1 = "0xA4"
int1 = int(str1,0)
flo1 = float(int1)
cmp1 = complex(int1,flo1)
str1 = str(cmp1)
str1 = "2+2"
str2 = repr(str1)
int1 = eval(eval(str2))
tupl2 = tuple(list1)
list2 = list(dict1)
set1 = set(list1)
dict2 = dict(F=1,S=2,T='ab')
print("dict2 is:",dict2)
fset1 = frozenset(tupl1)
char1 = chr(0x02A0)
int1 = ord('A')
int1 = hex(23)
int1 = oct(9)