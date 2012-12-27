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
# 1. Ensure clean text is extracted (beautiful soup doesn't work too
#	 well to get the text, and is bulky for a simple task. Just write 
#	 a simple parser to do this job (using maybe regex)
# 2. Output the files for clustering
#
# Bugs:
# 1. Text obtained isn't clean from html
#
#
#
#
########################################################################

from readability.readability import Document
import urllib
from bs4 import BeautifulSoup

# Change input and output file names here and give url
######################################################
inputFileName = 'rawInput.html'
outputFileName = 'readableOutput.html'
url = 'http://stackoverflow.com/questions/10486027/removing-html-image-tags-and-everything-in-between-from-a-string'
#######################################################

fpInFetch = open(inputFileName, 'w')
fpOut = open(outputFileName, 'w')
fpInFetch.write(urllib.urlopen(url).read())
fpInFetch.close()
fpIn = open( inputFileName, 'r')

# Fetching done, html doc stored

########################################################
# Now running beautiful soup

##########################################################

html = fpIn.read()
readableArticle = Document(html).summary()
readableTitle = Document(html).short_title()
soup = BeautifulSoup(readableArticle)
completeText = readableTitle + "\n\n" + soup.get_text()
fpOut.write(completeText.encode('ascii', 'ignore'))

# Remove all images from the article
# Assume you've got proper text only in the output file, now just
# make the XML file


