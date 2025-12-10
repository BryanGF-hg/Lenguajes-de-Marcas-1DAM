# pip3 install lxml --break-system-packages

from lxml import etree

xml_doc = etree.parse("006-curriculum deepseek.xml")
xsd_doc = etree.parse("005-esquema.xsd")

schema = etree.XMLSchema(xsd_doc)

print(schema.validate(xml_doc))
