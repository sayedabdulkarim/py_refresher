# https://www.example.com/
import requests;

result = requests.get("https://www.example.com/")

# print(result.text)

import bs4;

soup = bs4.BeautifulSoup(result.text, "lxml")
print(soup.select("p"))

# grabbing an image