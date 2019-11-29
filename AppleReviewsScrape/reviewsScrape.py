# refactor: create dictionary of namespaces, and loop through all xml files 
# even better: rss straight from this python file

import xml.etree.ElementTree as ET
import csv
from io import StringIO
import glob

tree = ET.parse("SparkSport-3.xml")
root = tree.getroot()

#open a file for writing

reviews = open('SparkSportReviews-3.csv', 'w')

#create the csv writer object

csvwriter = csv.writer(reviews)

#create object to store header
reviews_head = ["Title", "Author", "Content", "TimeStamp", "Rating"]

count = 0
#create a namespace dict

#iterate through tree, grab what we need
for member in root.findall("{http://www.w3.org/2005/Atom}entry"):
    entry = []

    if count == 0:
        csvwriter.writerow(reviews_head)
        count = count + 1
   
    title = member.find("{http://www.w3.org/2005/Atom}title").text
    entry.append(title)

    author = member.find("{http://www.w3.org/2005/Atom}author/{http://www.w3.org/2005/Atom}name").text
    entry.append(author)
   
    content = member.find("{http://www.w3.org/2005/Atom}content[@type='text']").text
    entry.append(content)
    
    timeStamp = member.find("{http://www.w3.org/2005/Atom}updated").text
    entry.append(timeStamp)

    rating = member.find("{http://itunes.apple.com/rss}rating").text
    entry.append(rating)
    
    csvwriter.writerow(entry)
reviews.close()





