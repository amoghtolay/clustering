'''
########################################################################
# Amogh Tolay
# Thursday, 27th December 2012
# This is a code to prepare html files for clustering
# What this does is as follows:
# 1. Fetches URL and reads the html to a file (Don't really require that
#	 presently only for debugging purposes)
# 2. Runs readability on this file, returns readable html
# 3. Run beautiful soup to extract text and then store just text in file
#    (Later remove beautiful soup, write own regex based cleaner)
# 4. Append this text only file to the XML file (after formatting)
# 5. Run clustering again on this XML file
#
#
#
# TODO:
# 1. Ensure clean text is extracted (beautiful soup and then nltk used).
# 	 If required use html2text.
# 2. Output the files for clustering
#
# Bugs:
# 1. Text obtained isn't clean from html
#
#
#
#
########################################################################
'''
from readability.readability import Document
import urllib
from bs4 import BeautifulSoup
import os.path
from xml.dom.minidom import Document as XMLDoc
import nltk

# IMPORTANT: CHANGE VARIABLES HERE
# Change input and output file names here and give url
########################################################################
inputFileName = 'rawInput.html'
outputFileName = 'readableOutput.html'
url = 'http://lifehacker.com/'
XMLFileName = 'xmlFileToCluster.xml'
########################################################################

'''
This function fetches HTML from URL and then saves this to the input
file given by inputFileName (contains raw data)
'''
def fetchURLandStore():
	fpInFetch = open(inputFileName, 'w')
	fpInFetch.write(urllib.urlopen(url).read())
	fpInFetch.close()

'''
This function opens the file containing HTML Code, then strips it
by running readability. After this, beuatiful soup (followed by nltk)
reads it and extracts title and text separately.
This funtion ultimately gives a list containing plain text 
[heading, data] and returns it
'''
def extractReadableText():
	fpIn = open( inputFileName, 'r')
	fpOut = open(outputFileName, 'w')

	html = fpIn.read()
	readableArticle = Document(html).summary()
	readableTitle = Document(html).short_title()
	
	soup = BeautifulSoup(readableArticle)
	completeText = [ readableTitle, nltk.clean_html( ''.join(soup.findAll(text=True)) ) ]
	
	return completeText

'''
Call this function if you need to create the XML File. 
This will be called only once for any user, as it happens only for
the first bookmarked link
'''
def createXML ( completeText, url ):
	# Create the minidom document
	doc = XMLDoc()
	autoID = 0

	# Create the <searchresult> base element
	searchresult = doc.createElement("searchresult")
	doc.appendChild(searchresult)

	# Create the <document> element (1 for each URL)
	mainElemDoc = doc.createElement("document")
	mainElemDoc.setAttribute("id", str(autoID))
	searchresult.appendChild(mainElemDoc)

	# Create a <title> element
	title = doc.createElement("title")
	mainElemDoc.appendChild(title)
	# Give the <title> elemenet some text
	titleText = doc.createTextNode( completeText[0].encode('ascii', 'ignore') )
	title.appendChild(titleText)

	# Create a <url> element
	urlField = doc.createElement("url")
	mainElemDoc.appendChild(urlField)
	# Give the <url> elemenet some text
	urlText = doc.createTextNode( url )
	urlField.appendChild(urlText)

	# Create a <snippet> element
	snippet = doc.createElement("snippet")
	mainElemDoc.appendChild(snippet)
	# Give the <snippet> elemenet some text
	snippetText = doc.createTextNode( completeText[1].encode('ascii', 'ignore') )
	snippet.appendChild(snippetText)

	# Print our newly created XML
	fp = open(XMLFileName, 'w')
	entireXMLFile = doc.toprettyxml(indent = "    ")
	fp.write(entireXMLFile)

########################################################################
# Call this function if your XML File already exists.
# It parses the XML file, sees the autoID of the document, and appends
# this document to the XML file appropriately.
# This function is always called except for 1st bookmark
########################################################################
# def appendXML ( completeText ):
	

def main():
	fetchURLandStore()
	completeText = extractReadableText()
	print completeText
	if os.path.isfile(XMLFileName):
		appendXML ( completeText, url )
	else:
		createXML ( completeText, url )
		
		
main()
