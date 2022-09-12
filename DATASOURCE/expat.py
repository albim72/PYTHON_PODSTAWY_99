import xml.parsers.expat

def first_element(tag,attrs):
    print(f'first element: {tag}, {attrs}')

def last_element(tag):
    print(f'last element: {tag}')

def character_value(value):
    print(f'character value: {repr(value)}')

parser_expat = xml.parsers.expat.ParserCreate()

parser_expat.StartElementHandler = first_element
parser_expat.EndElementHandler = last_element
parser_expat.CharacterDataHandler = character_value
file = open("student.xml","r",encoding="utf-8")
xmlstr = file.read()
parser_expat.Parse(xmlstr,1)
