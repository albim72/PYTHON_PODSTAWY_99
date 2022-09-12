import xml.etree.ElementTree as ET

try:
    tree = ET.parse("kraj.xml")
    root = tree.getroot()

    #wyświetl wszystkie dzieci taga root z ich nazwami i atrybutami

    for child in root:
        print(f"nazwa taga: {child.tag}, atrybuty: {child.attrib}")

    print(root[0][2].text)
except:
    print("element nie istnieje")
