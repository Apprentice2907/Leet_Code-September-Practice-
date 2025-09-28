'''You are given an alphanumeric string s. (Alphanumeric string is a string consisting of lowercase English letters and digits).

You have to find a permutation of the string where no letter is followed by another letter and no digit is followed by another digit. That is, no two adjacent characters have the same type.

Return the reformatted string or return an empty string if it is impossible to reformat the string.

 

Example 1:

Input: s = "a0b1c2"
Output: "0a1b2c"
Explanation: No two adjacent characters have the same type in "0a1b2c". "a0b1c2", "0a1b2c", "0c2a1b" are also valid permutations.
Example 2:

Input: s = "leetcode"
Output: ""
Explanation: "leetcode" has only characters so we cannot separate them by digits.
Example 3:

Input: s = "1229857369"
Output: ""
Explanation: "1229857369" has only digits so we cannot separate them by characters.'''







# my logic using condition

class Solution(object):
    def reformat(self, s):
        """
        :type s: str
        :rtype: str
        """
        digits = []
        letters = []
        
        for ch in s:
            if ch.isdigit():
                digits.append(ch)
            else:
                letters.append(ch)
        
        if abs(len(digits) - len(letters)) > 1:
            return ""
        
        if len(digits) > len(letters):
            first, second = digits, letters
        else:
            first, second = letters, digits
        
        result = []
        for i in range(len(s)):
            if i % 2 == 0:
                result.append(first.pop())
            else:
                result.append(second.pop())
        
        return "".join(result)
    






# Leet code optimal solution

import math
class Solution(object):
    def reformat(self, s):
        lett=[]
        nums=[]
        for i in s:
            if i.isalpha():
                lett.append(i)
            else: nums.append(i)
        if abs(len(lett)-len(nums))>1: return ""
        ans=""
        for i in range(min(len(lett),len(nums))):
            ans+=lett[i]
            ans+=nums[i]
        if len(lett)>len(nums): return ans+lett[-1]
        elif len(nums)>len(lett): return nums[-1]+ans
        return ans
        """
        :type s: str
        :rtype: str
        """
        