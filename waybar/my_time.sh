#!/bin/bash

# Gregorian & Jalali ( Hijri_Shamsi , Solar ) Date Converter  Functions
# Author: JDF.SCR.IR =>> Download Full Version :  http://jdf.scr.ir/jdf
#modifide by mohammad hashemy to show curent day of the month
# License: GNU/LGPL _ Open Source & Free :: Version: 2.80 : [2020=1399]
# ---------------------------------------------------------------------
# 355746=361590-5844 & 361590=(30*33*365)+(30*8) & 5844=(16*365)+(16/4)
# 355666=355746-79-1 & 355668=355746-79+1 &  1595=605+990 &  605=621-16
# 990=30*33 & 12053=(365*33)+(32/4) & 36524=(365*100)+(100/4)-(100/100)
# 1461=(365*4)+(4/4)   &   146097=(365*400)+(400/4)-(400/100)+(400/400)

gregorian_to_jalali(){
    gy=$1; gm=$2; gd=$3
    g_d_m=(0 31 59 90 120 151 181 212 243 273 304 334)
    if [ $gm -gt 2 ]; then
        gy2=$((gy + 1))
    else
        gy2=$gy
    fi
    days=$((355666 + (365 * gy) + ((gy2 + 3) / 4) - ((gy2 + 99) / 100) + ((gy2 + 399) / 400) + gd + g_d_m[gm - 1]))
    jy=$((-1595 + (33 * (days / 12053))))
    days=$((days % 12053))
    jy=$((jy + (4 * (days / 1461))))
    days=$((days % 1461))
    if [ $days -gt 365 ]; then
        jy=$((jy + ((days - 1) / 365)))
        days=$(((days - 1) % 365))
    fi
    if [ $days -lt 186 ]; then
        jm=$((1 + (days / 31)))
        jd=$((1 + (days % 31)))
    else
        jm=$((7 + ((days - 186) / 30)))
        jd=$((1 + ((days - 186) % 30)))
    fi
    jalali=($jy $jm $jd)
}


# gregorian_to_jalali 2020 6 14;
# echo ${jalali[0]}/${jalali[1]}/${jalali[2]};

day="$(date "+%d")";
day=$(echo $day | sed 's/^0*//')
month=$(date "+%m");
month=$(echo $month | sed 's/^0*//')
year="$(date "+%Y")";
    
gregorian_to_jalali $year $month $day;
echo "$(date "+%a") -" ${jalali[2]} " | $(date "+%l:%M %p")"

