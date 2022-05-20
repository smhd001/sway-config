#!/usr/bin/env python3
import requests
import subprocess
import os
from shutil import copyfile
url = "https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-US"
path = os.path.expanduser("~/Pictures/wallpaper/bing_bg/")
#https://bing.com/th?id=OHR.Italica_EN-US1640838317_1920x1080.jpg&rf=LaDigue_1920x1080.jpg&pid=hp

try:
    r = requests.get(url)
    url = "https://bing.com" + r.json()["images"][0]["url"]

    name = url[url.index("?id=OHR.") + 8:url.index("_EN-US")] + ".jpg"
    print(name.split(".")[0])
    info = r.json()["images"][0]["copyright"]

    #check if last line is the same as the info
    with open(path + "info.txt","r") as f:
        if f.readlines()[-1] != info + "\n":
            new = True
        else:
            new = False
except Exception:
    print("no internet")
    with open(path + "info.txt", "r") as f:
        info = f.readlines()[-1][:-1]
    new = False
    name = ""

print(info)

#append info to file
if new:
    img = requests.get(url)
    with open(path + name,"wb") as f:
        f.write(img.content)
    with open(path + "info.txt","a") as f:
        date = r.json()["images"][0]["startdate"] 
        date = date[:4] + "-" + date[4:6] + "-" + date[6:]
        f.write("[ " + date + " ] | " + (name).split(".")[0] + ":\n")
        f.write( info + "\n")
        subprocess.run(["dunstify",name.split(".")[0],info ,"-t","9000"])
    copyfile(path + name ,path + "backg")


subprocess.run(["swaymsg","output * bg " + path + "backg fill"])

#subprocess.run(["convert",name,"-resize","1366x768",path +"backg"])
