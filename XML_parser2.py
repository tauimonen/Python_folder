# Parsing a simple XML file

import xml.etree.ElementTree as et

data = '''<?xml version="1.0" encoding="UTF-8" ?>
<metadata>
    <test>
        <item name="item">troot</item>
        <price>€100</price>
        <description>
            tottoroo
        </description>
         <calories>553</calories>
    </test>
</metadata>'''

myroot = et.fromstring(data)
print(myroot.tag)