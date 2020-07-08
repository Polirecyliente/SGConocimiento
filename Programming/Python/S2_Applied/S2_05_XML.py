#!/usr/bin/python3
#   XML

#T# XML processing

#T# import DOM API
import xml.dom.minidom

fileXML = """/home/jul/PolirecylBases/\
tutos/Python/Section2/Section2_5Debug.xml"""

#T# parse XML file into a DOM object with parse()
DOMTree1 = xml.dom.minidom.parse(fileXML)

#T# get the root element with documentElement of the DOM object
project1 = DOMTree1.documentElement
print("Root element:",project1)

#T# get an attribute of an element with getAttribute()
print("Project name:",project1.getAttribute("name"))

#T# get child elements by their tag names with getElementsByTagName()
views1 = project1.getElementsByTagName("view")

#T# iterate over child elements
for view1 in views1:
    print("viewID:",view1.getAttribute("id"))
    if view1.getElementsByTagName("description"):

#T# access the contents of an element with childNodes[0].data
        descr1 = view1.getElementsByTagName("description")[0]
        print("Project description:",descr1.childNodes[0].data)