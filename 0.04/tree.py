import lxml.etree as le

with open('simple.xml','r') as f:
    doc=le.parse(f)
    for elem in doc:
            parent=elem.getparent()
            parent.remove(elem)
    print(le.tostring(doc))