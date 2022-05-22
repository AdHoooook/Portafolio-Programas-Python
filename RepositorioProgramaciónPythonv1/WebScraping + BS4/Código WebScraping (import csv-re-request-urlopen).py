


#!/usr/bin/python

import csv
from urllib import urlopen
import re
import requests 

# Open and read html/xml

xml = urlopen("https://www.gotspaceusa.com/properties/#view=7,34.39331222316112,-105.97412109375").read()

# Grab article titles and urls using regex

xmlTitle = re.compile("<title>(.*)</title>")
xmlLink = re.compile("<link>(.*)</link>")

# Store the Data 

findTitle = re.findall(xmlTitle,xml)
findLink = re.findall(xmlLink,xml)

# Iterate through the articles to create a range

iterate = []
iterate[:] = range(1, 369)

# Open the CSV file, write the headers

writer = csv.writer(open("pytest.csv","wb"))
head = ("Title", "URL")
writer.writerow(head)

# Write the results to the CSV file

for i  in iterate:
    writer.writerow([findTitle[i], findLink[i]])
    
