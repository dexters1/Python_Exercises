import os
from lxml import etree
from lxml import objectify

file_name = "countries.xml"

file = open(file_name, 'rb')

tree = objectify.parse(file)

file.close()

country = tree.findall("country")

print("List of countries in xml file:\n")
for c in country:
    print(c.get("name"))

root = tree.getroot()
tmp = etree.SubElement(root,'country')
tmp.set("name", "Serbia")
rank = etree.SubElement(tmp, 'rank')
rank._setText('99')

country = tree.findall("country")

print("\nList of countries in xml file after addition:\n")
for c in country:
    print(c.get("name"))

tree.write(open('new_xml.xml', 'w'), encoding='utf-8')

print("\npretty_print of content in the new xml file: \n")    
print(etree.tostring(root, pretty_print = True))
 