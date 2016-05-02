import requests
from bs4 import BeautifulSoup

url = "https://www.hackerrank.com/contests"
r = requests.get(url)

soup = BeautifulSoup(r.content,"html.parser")

links = soup.find_all("a")

for link in links:
        if "http" in link.get("href"):
                print("<a href='%s'>%s</a>" %(link.get("href"),link.text))

g_data = soup.find_all("div", {"class": "clearfix"})

for item in g_data:
        print(item)
