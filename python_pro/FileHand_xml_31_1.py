import xml.etree.ElementTree as ET

root = ET.Element("people")
person1 = ET.SubElement(root, "person", name="Japan")
person2 = ET.SubElement(root, "person", name="ABC")

tree = ET.ElementTree(root)
tree.write("people.xml")

#Reading the XML file
tree = ET.parse("people.xml")
root = tree.getroot()

print("Reading XML:")
for person in root.findall("person"):
    name = person.get("name")
    print(f"Name: {name}")

person1 = ET.SubElement(root, "person", name="A")
person2 = ET.SubElement(root, "person", name="B")

tree = ET.ElementTree(root)
tree.write("people.xml")

print("XML file 'people.xml' created successfully.")