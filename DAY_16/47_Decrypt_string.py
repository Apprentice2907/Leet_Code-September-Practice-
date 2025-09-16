'''ou are given a string s formed by digits and '#'. We want to map s to English lowercase characters as follows:
Characters ('a' to 'i') are represented by ('1' to '9') respectively.
Characters ('j' to 'z') are represented by ('10#' to '26#') respectively.
Return the string formed after mapping.
The test cases are generated so that a unique mapping will always exist.

Example 1:

Input: s = "10#11#12"
Output: "jkab"
Explanation: "j" -> "10#" , "k" -> "11#" , "a" -> "1" , "b" -> "2".
Example 2:

Input: s = "1326#"
Output: "acz"
 '''





# My logic using reverse traversal logic and also best leet code solution

class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = ""
        i = len(s) - 1
        while i >= 0:
            if s[i] == '#':
                num = int(s[i-2:i])   
                ans = chr(96 + num) + ans
                i -= 3
            else:
                num = int(s[i])
                ans = chr(96 + num) + ans
                i -= 1
        return ans





# My logic using split and then checking every individual

class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = ""
        parts = s.split('#')
        for i in range(len(parts)):
            if i < len(parts) - 1:
                num = int(parts[i][-2:])
                ans += chr(96 + num)
                for ch in parts[i][:-2]:
                    ans += chr(96 + int(ch))
            else:
                for ch in parts[i]:
                    ans += chr(96 + int(ch))
        return ans
