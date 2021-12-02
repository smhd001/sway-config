#!/usr/bin/env python3
from os import write
import requests
import subprocess
import os
from shutil import copyfile
url = "https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-US"
#https://bing.com/th?id=OHR.Italica_EN-US1640838317_1920x1080.jpg&rf=LaDigue_1920x1080.jpg&pid=hp
r = requests.get(url)
url = "https://bing.com" + r.json()["images"][0]["url"]
print(url)
img = requests.get(url)
path = os.path.expanduser("~/Pictures/wallpaper/bing_bg/")
name = url[url.index("?id=OHR.") + 8:url.index("_EN-US")] + ".jpg"
name = path + name
with open(name,"wb") as f:
    f.write(img.content)
#subprocess.run(["convert",name,"-resize","1366x768",path +"backg"])
print("name:",name.split("/")[-1])
copyfile(name,path + "backg")
subprocess.run(["swaymsg","output * bg " + path + "backg fill"])
