'''Given a date, return the corresponding day of the week for that date.

The input is given as three integers representing the day, month and year respectively.

Return the answer as one of the following values {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}.

 

Example 1:

Input: day = 31, month = 8, year = 2019
Output: "Saturday"
Example 2:

Input: day = 18, month = 7, year = 1999
Output: "Sunday"
Example 3:

Input: day = 15, month = 8, year = 1993
Output: "Sunday"'''







# My logic without module 

class Solution(object):
    def dayOfTheWeek(self, day, month, year):
        """
        :type day: int
        :type month: int
        :type year: int
        :rtype: str
        """
        week = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

        if month == 1:
            month = 13
            year -= 1
        elif month == 2:
            month = 14
            year -= 1

        k = year % 100
        j = year // 100

        h = (day + (13 * (month + 1)) // 5 + k + k // 4 + j // 4 + 5 * j) % 7

        return week[h]








# my logic using datetime module and also leet code best solution

class Solution(object):
    def dayOfTheWeek(self, day, month, year):
        """
        :type day: int
        :type month: int
        :type year: int
        :rtype: str
        """
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        d = datetime.date(year, month, day)
        return days[d.weekday()]
    






# Another logic without inbuilt module

class Solution(object):
    def dayOfTheWeek(self, day, month, year):
        """
        :type day: int
        :type month: int
        :type year: int
        :rtype: str
        """
        def hasLeapDay(year):
			return True if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else False
        odd_days=[31,28,31,30,31,30,31,31,30,31,30,31]
        weekdays=["Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"]
        total_days=0
       
        for i in range(1971,year):
            total_days+=366 if hasLeapDay(i) else 365

        for j in range(month-1):
            total_days+=odd_days[j]

        if month>2:
            total_days+=1 if hasLeapDay(year) else 0
        
        total_days+=day-1
        return weekdays[total_days%7]