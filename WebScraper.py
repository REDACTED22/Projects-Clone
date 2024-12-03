import requests
from bs4 import BeautifulSoup


# Making a GET request
r = requests.get('https://www.police.psu.edu/daily-crime-log')

# check status code for response received
# success code - 200
print(r)

# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')
soup=soup.prettify()
#print(soup)
for line in soup:
    for word in line:
        # Check if the line starts with "python" (case-sensitive)
        if word.lower()=='theft':
            print(line.strip())