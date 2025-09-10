'''Given a string date representing a Gregorian calendar date formatted as YYYY-MM-DD, return the day number of the year.

Example 1:

Input: date = "2019-01-09"
Output: 9
Explanation: Given date is the 9th day of the year in 2019.
Example 2:

Input: date = "2019-02-10"
Output: 41'''






# My logic using mapping method

class Solution(object):
    def dayOfYear(self, date):
        """
        :type date: str
        :rtype: int
        """
        year, month, day = map(int, date.split('-'))
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
            days_in_month[1] = 29

        return sum(days_in_month[:month - 1]) + day
    





# Leet code best solution

class Solution(object):
    def dayOfYear(self, date):
        """
        :type date: str
        :rtype: int
        """
        yr=[0,31,59,90,120,151,181,212,243,273,304,334]
        day=int(date[-2:])
        year=int(date[:4])
        month=int(date[5:7])

        if year%4==0 and year!=1900 and month>2:
            day+=1
        return yr[month-1]+day