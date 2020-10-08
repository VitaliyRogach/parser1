import requests
from bs4 import BeautifulSoup

url = "https://habr.com/ru/post/399683/"

response = requests.get(url)

html = response.text

soup = BeautifulSoup(html, "html.parser")

conteiner = soup.find("div", {"class":"post__text post__text-html post__text_v1"})
elements = conteiner.find_all("b")

sp = [(element.text) for element in elements]
print(sp)

with open("out.TXT","w", encoding="utf8") as f:
    f.write(str(sp))