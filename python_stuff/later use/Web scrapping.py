from bs4 import BeautifulSoup
import requests
import csv

page_to_scrape = requests.get ("https://quotes.toscrape.com/")
soup = BeautifulSoup (page_to_scrape.content, "html.parser")
quotes = soup.findAll ("span", attrs={"class": "text"})
authors = soup.findAll ("small", attrs={"class": "author"})

file = open ("quotes.csv", "w")
writer = csv.writer (file)
writer.writerow (["Quotes", "Authors"])


#for words in authors:
    #print (words.text)
#for author in authors:
    #print (author.text)
    
for quotes, authors in zip (quotes, authors):
    print (quotes.text + " - " + authors.text)
    writer.writerow ([quotes.text, authors.text])
file.close ()
    
