#include <stdio.h>
#include <ctime>

/**  Gregorian & Jalali (Hijri_Shamsi,Solar) Date Converter Functions
Author: JDF.SCR.IR =>> Download Full Version :  http://jdf.scr.ir/jdf
License: GNU/LGPL _ Open Source & Free :: Version: 2.80 : [2020=1399]
---------------------------------------------------------------------
**/
int gregorian_to_jalali(int gy, int gm, int gd)
{
    int days;
    {
        int gy2 = (gm > 2) ? (gy + 1) : gy;
        int g_d_m[12] = {0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334};
        days = 355666 + (365 * gy) + ((int)((gy2 + 3) / 4)) - ((int)((gy2 + 99) / 100)) + ((int)((gy2 + 399) / 400)) + gd + g_d_m[gm - 1];
    }
    days %= 12053;
    days %= 1461;
    if (days > 365)
    {
        days = (days - 1) % 365;
    }
    if (days < 186)
    {
        return 1 + (days % 31); /*jd*/
    }
    else
    {
        return 1 + ((days - 186) % 30); /*jd*/
    }
}
int main(int argc, char const *argv[])
{
    using namespace std;
    int day;
    time_t t = time(0);
    tm *now = std::localtime(&t);
    day = gregorian_to_jalali(1900 + now->tm_year, now->tm_mon + 1, now->tm_mday);
    const char *w_d;
    switch (now->tm_wday)
    {
    case 0:
        w_d = "Sun";
        break;
    case 1:
        w_d = "Mon";
        break;
    case 2:
        w_d = "Tue";
        break;
    case 3:
        w_d = "Wed";
        break;
    case 4:
        w_d = "Thu";
        break;
    case 5:
        w_d = "Fri";
        break;
    case 6:
        w_d = "Sat";
        break;
    default:
        w_d = "ERO";
        break;
    }
    const char *AMPM;
    int hour = now->tm_hour;
    if (hour > 12)
    {
        hour %= 12;
        AMPM = "PM";
    }
    else
    {
        AMPM = "AM";
    }
    //"$(date "+%a") -" ${jalali[2]} " | $(date "+%l:%M %p")"
    printf("%s - %d  |  %02d:%02d %s", w_d, day, hour, now->tm_min, AMPM);
    return 0;
}
