from bs4 import BeautifulSoup
import urllib2

#Create soup object from given url in read mode
soup = BeautifulSoup(urllib2.urlopen("http://fastcompany.com").read())

#create list of scraped urls
list_of_links = [link.get('href') for link in soup.find_all('a')]

#print out sorted list of urls 
print '\n'.join(sorted(list_of_links))





 
  





 

