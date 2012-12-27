This is part of a tool that I plan to design. The function of codes in this repo is to extract HTML code from URLs, then use readability ( http://lab.arc90.com/experiments/readability/ ) to obtain a readable page consisting of only meaningful data (removes ads. comments and other unrelated text. It keeps only the useful contents that usually people read).
Though readability works pretty well, its not 100% accurate. After this HTML file is made, extract only the contents from the file, and then convert it into an XML file. Now a set of URLs will be scraped and the XML file would contain data from all URLs. Then cluster the URLs based on topics using Carrot Document Clustering Server ( http://project.carrot2.org ).

This is just a first attempt and is a small part of a bigger project. At present, it is buggy but I plan to work on this, so hopefully it will be better in the future! :)
