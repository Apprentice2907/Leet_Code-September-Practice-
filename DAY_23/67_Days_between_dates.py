'''Write a program to count the number of days between two dates.
The two dates are given as strings, their format is YYYY-MM-DD as shown in the examples.

Example 1:

Input: date1 = "2019-06-29", date2 = "2019-06-30"
Output: 1
Example 2:

Input: date1 = "2020-01-15", date2 = "2019-12-31"
Output: 15
 '''



# My logic using UDF and also optimal solution

class Solution(object):
    def leapyear(self, year):
        return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

    def daysmonth(self, year, month):
        if month == 2:
            return 29 if self.leapyear(year) else 28
        elif month in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        else:
            return 30

    def days1971(self, date):
        year, month, day = map(int, date.split('-'))
        days = 0
        
        for y in range(1971, year):
            days += 366 if self.leapyear(y) else 365
        
        for m in range(1, month):
            days += self.daysmonth(year, m)

        days += day
        return days

    def daysBetweenDates(self, date1, date2):
        return abs(self.days1971(date1) - self.days1971(date2))
    






# Leetcode best solution

from datetime import datetime

class Solution(object):
    def daysBetweenDates(self, date1, date2):
        epoch = datetime(1970, 1, 1)
        dt1 = datetime.strptime(date1, "%Y-%m-%d")
        dt2 = datetime.strptime(date2, "%Y-%m-%d")
        return abs((dt2-dt1).days)
        """
        :type date1: str
        :type date2: str
        :rtype: int
        """





    
# Simple logic and easy to understand

class Solution(object):
    def daysBetweenDates(self, date1, date2):
        y1, m1, d1 = map(int, date1.split('-'))
        y2, m2, d2 = map(int, date2.split('-'))

        if (y1, m1, d1) > (y2, m2, d2):
            y1, m1, d1, y2, m2, d2 = y2, m2, d2, y1, m1, d1

        mdays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def is_leap(year):
            return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

        count = 0
        while (y1, m1, d1) != (y2, m2, d2):
            d1 += 1
            if m1 == 2 and is_leap(y1):
                end_day = 29
            else:
                end_day = mdays[m1 - 1]

            if d1 > end_day:
                d1 = 1
                m1 += 1
                if m1 > 12:
                    m1 = 1
                    y1 += 1
            count += 1
        return count