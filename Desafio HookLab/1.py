from bs4 import BeautifulSoup
import requests
import csv

source = requests.get("https://www.reddit.com/r/programming/")

soup = BeautifulSoup(source.text, "html.parser")

posts = soup.find_all("div", class_="_1oQyIsiPHYt6nx7VOmd1sz", limit=3)


print(len(posts))
