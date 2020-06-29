import requests
import urllib3
from urllib.parse import quote
from bs4 import BeautifulSoup
import json
import re


base = "https://api.genius.com/"
ss = "search?q="
Song = quote("free porn cheap drugs")
token = "&access_token=1wsoiHas6wuszSvEKNWofVuD9NKiXnXXWzeuwayw3I56CIoGIakOv1ecbYzO4mfW"

Qstring = base + ss + Song + token

res = requests.get(Qstring)
src = res.json()

options = {}

for i in src['response']['hits']:
    name_title  = (i["result"]["primary_artist"]["name"]) + ":" + " " +   (i["result"]["title_with_featured"])
    api_bruh = (i["result"]["api_path"])
    options[name_title] = api_bruh



d = 1
song_id = list(options.values())
for i in options:
    print(f"{d}.{i}")
    d+=1


def picking():
    while True:
        cho = int(input("Enter Song Number "))
        try:
            song_url = song_id[cho-1]
            return song_url
        except:
            print("Incorrect Number Bruh")
            return picking()

'''def picking():
    cho = int(input("Enter Song Number "))
    try:
        while cho != song_id.index(song_id[cho-1]): [Althernative way but other way is better??]
            song_url = song_id[cho-1]
            return song_url
    except:
        print("Incorrect Number Bruh")
        return picking()'''


SongURL = f"https://genius.com{picking()}{token}"
Res_1 = requests.get(SongURL)


soup = BeautifulSoup(Res_1.text, "html5lib")



while True:
    try:
        lyrics = soup.find("div", class_="lyrics").get_text()
        print(lyrics)
        break
    except Exception:
        print("Loading...")

## Works But not the best, but yeah lyrics can be extracted
















