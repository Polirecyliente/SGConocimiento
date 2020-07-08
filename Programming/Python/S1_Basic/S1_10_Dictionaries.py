#!/usr/bin/python3
#   Dictionaries

#T# declaration, updating, and accessing
dict1 = {'key1':5,'key2':'val2'}
dict1['keyNew'] = 'newV'
print(dict1['keyNew'])

#T# clear the whole dictionary with clear()
dict1.clear()
print(dict1)

dict2 = {'key1':7,'key2':'val2'}
#T# dictionary functions
print("dict with str representation:",str(dict2))
print("type of dict var is: ",type(dict2))
dict3 = dict2.copy()
print("new dict: ",dict3)
tupl1 = ('tupK1','valNo')
dict4 = dict.fromkeys(tupl1,8)
print("dict from keys:",dict4)
print("value from key \'key2\'",dict2.get('key2'))
print("dict's items:",dict2.items())
print("dict's keys:",dict2.keys())
print("dict's values:",dict2.values())

#T# append a dictionary to another with dict1.update(dictAppended)
dict2.update(dict4)
print("append a dict to another:",dict2)
dict2.setdefault('noKey','defVal')
print("default value:",dict2['noKey'])