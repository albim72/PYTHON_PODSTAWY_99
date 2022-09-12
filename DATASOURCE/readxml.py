from xml.dom.minidom import parse

dom = parse("dane.xml")
name = dom.getElementsByTagName('name')
kod = dom.getElementsByTagName('kod')
adres = dom.getElementsByTagName('adres')

print(" ".join(t.nodeValue for t in name[0].childNodes if t.nodeType == t.TEXT_NODE))
print(" ".join(t.nodeValue for t in kod[0].childNodes if t.nodeType == t.TEXT_NODE))
print(" ".join(t.nodeValue for t in adres[0].childNodes if t.nodeType == t.TEXT_NODE))
print(" ".join(t.nodeValue for t in kod[1].childNodes if t.nodeType == t.TEXT_NODE))
