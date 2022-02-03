# Parsing a simple XML file

import xml.etree.ElementTree as et

mytree = et.parse('Sample.xml')
myroot = mytree.getroot()
print(myroot.tag)
print(myroot[0].attrib)

for i in myroot[0]:
    print(i.tag, i.attrib)
print(20 * "=")
for i in myroot[0]:
    print(i.text)