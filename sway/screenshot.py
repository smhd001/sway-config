#!/usr/bin/env python3
from datetime import datetime
import os
from os.path import expanduser
import sys
from time import sleep

#deafult area for screenshot
d_area = "s"
#for save/copy/show
d_act =  "c"

d_path = "~/Pictures/screenshot"

def gregorian_to_jalali(gy, gm, gd):
    g_d_m = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
    if (gm > 2):
        gy2 = gy + 1
    else:
        gy2 = gy
    days = 355666 + (365 * gy) + ((gy2 + 3) // 4) - ((gy2 + 99) //
                                                     100) + ((gy2 + 399) // 400) + gd + g_d_m[gm - 1]
    jy = -1595 + (33 * (days // 12053))
    days %= 12053
    jy += 4 * (days // 1461)
    days %= 1461
    if (days > 365):
        jy += (days - 1) // 365
        days = (days - 1) % 365
    if (days < 186):
        jm = 1 + (days // 31)
        jd = 1 + (days % 31)
    else:
        jm = 7 + ((days - 186) // 30)
        jd = 1 + ((days - 186) % 30)
    return [jy, jm, jd]


def get_name():
    miladi = datetime.today().strftime('%Y%m%d_%H%M')
    jalali = gregorian_to_jalali(
        int(miladi[:4]), int(miladi[4:6]), int(miladi[6:8]))
    return "/Sc_" + str(jalali[0]) + f"{jalali[1]:02d}" + f"{jalali[2]:02d}_" + miladi + ".png"


def dmenu_chose() -> str:
    a = os.popen("echo " + "\"" "" "\"" + "|" +
                 "dmenu -p a:whole,s:select,w:window,v:save,c:copy,e:see")
    return a.read()


def take():
    if 'v' in ord:
        path = expanduser(d_path)
    else:
        path = "/tmp"

    name = path + get_name()
    print(name)
    print("grim" + " " + options + " " + name)
    if not (os.system("grim" + " " + options + " " + name)):
        if "c" in ord:
            os.popen("wl-copy < " + name)
        if "e" in ord:
            os.popen("imv-wayland " + name)


if __name__ == "__main__":
    if(len(sys.argv) == 1):
        ord = dmenu_chose()
        if(ord == ""):
            sys.exit(0)
    else:
        ord = "".join(sys.argv[1:])

    if not("a" in ord or "s" in ord or "w" in ord):
        ord += d_area

    if not("v" in ord or "c" in ord or "e" in ord):
        ord += d_act

    if "a" in ord:
        options = ""
    if "s" in ord:
        options = "-g \"$(slurp)\""
    if "w" in ord:
        options = "-g \"$(swaymsg -t get_tree | jq -j \'.. | select(.type?) | select(.focused).rect | \"\(.x),\(.y) \(.width)x\(.height)\"\')\""
    take()
