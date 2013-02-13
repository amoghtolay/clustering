from xml.dom.minidom import Document as XMLDoc
from elementtree import ElementTree as ET
from xml.etree.ElementTree import fromstring, ElementTree, Element

XMLFileName = 'xmlFileToCluster.xml'
tree = ET.parse(XMLFileName)
root = tree.getroot()
maxID = 0
for child in root:
	if maxID < int( child.attrib['id'] ):
		maxID = int( child.attrib['id'] )
newID = maxID + 1
print newID

# Now append a new entry to this tree, and then write file


tree.write(XMLFileName)
