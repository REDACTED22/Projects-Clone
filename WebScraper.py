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
file = open("Web.txt", "w")
file.write(soup)


def get_lines_containing_word(file_path, word):
    matching_lines = []
    with open('Web.txt', "r") as file:
        for line in file:
            # Check if the word is in the line
            if word in line:
                matching_lines.append(line.strip())  # Add to the list without extra whitespace
    return matching_lines



file.close