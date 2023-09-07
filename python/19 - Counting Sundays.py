'''You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?'''


def leapyear(year):
    return True if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else False



months = {'Jan': 31, 'Fev': 28, 'Mar': 31, 'April': 30, 'May': 31, 'June': 30, 'July': 31, 'Aug': 31, 'Sept': 30, 'Oct': 31, 'Nov': 30, 'Dec': 31}
week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
count = 0
wek = 0
for y in range(1901, 2000+1):
    months['Fev'] = 29 if leapyear(y) else 28
    for m in months.keys():
        for d in range(1, months[m]+1):
            if week[wek] == 'Monday' and d == 1:
                count += 1
            if wek < 6:
                wek += 1
            else:
                wek = 0


print(count)



import datetime

count = 0
for y in range(1901, 2000+1):
    for m in range(1, 12+1):
        if datetime.datetime(y, m, 1).weekday() == 6:
            count += 1
print(count)