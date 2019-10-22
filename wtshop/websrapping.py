from bs4 import BeautifulSoup
import requests

request = request.get('')
html = request.text 
soup = BeautifulSoup(html, "html.parser")

print(soup.find_all)
print(soup.find("tag", class="", ))
