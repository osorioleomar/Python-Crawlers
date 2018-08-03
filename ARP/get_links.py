import requests
from bs4 import BeautifulSoup
import sys

headers = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"}
page = requests.get(str(sys.argv[1]),headers=headers)

soup = BeautifulSoup(page.text, "html.parser")

#Pull all the iframes
iframes = soup.find_all('iframe')

if len(iframes):
    print("\nFound " + str(len(iframes)) + " iframe(s).\n")
    print("Found the following links:\n")
else:
    print("\nNo links found.\n")

for iframe in iframes:
    print("        " + iframe['src'])
    print("")
