'''For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).
Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""'''







# My logic and leet code best solution

class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        if str1 + str2 != str2 + str1:
            return ""
        n = min(len(str1), len(str2))
        for i in range(n, 0, -1):
            if len(str1) % i == 0 and len(str2) % i == 0:
                candidate = str1[:i]
                if candidate * (len(str1)//i) == str1 and candidate * (len(str2)//i) == str2:
                    return candidate
        return ""
    







# SImple logic

class Solution(object):
    def gcdOfStrings(self,str1, str2):
        if str1 + str2 != str2 + str1:
            return ""
        n = min(len(str1), len(str2))
        for i in range(n, 0, -1):
            part = str1[:i]
            if str1 == part * (len(str1) // i) and str2 == part * (len(str2) // i):
            return part
    return ""
