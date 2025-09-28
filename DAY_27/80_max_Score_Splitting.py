'''Given a string s of zeros and ones, return the maximum score after splitting the string into two non-empty substrings (i.e. left substring and right substring).

The score after splitting a string is the number of zeros in the left substring plus the number of ones in the right substring.

 

Example 1:

Input: s = "011101"
Output: 5 
Explanation: 
All possible ways of splitting s into two non-empty substrings are:
left = "0" and right = "11101", score = 1 + 4 = 5 
left = "01" and right = "1101", score = 1 + 3 = 4 
left = "011" and right = "101", score = 1 + 2 = 3 
left = "0111" and right = "01", score = 1 + 1 = 2 
left = "01110" and right = "1", score = 2 + 1 = 3
Example 2:

Input: s = "00111"
Output: 5
Explanation: When left = "00" and right = "111", we get the maximum score = 2 + 3 = 5
Example 3:

Input: s = "1111"
Output: 3'''




# My logic using loop and condition

class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        max_score = 0
        
        for i in range(1, n):  
            left = s[:i]
            right = s[i:]
            
            zeros = 0
            ones = 0
            
            for ch in left:
                if ch == '0':
                    zeros += 1
            
            for ch in right:
                if ch == '1':
                    ones += 1
            
            score = zeros + ones
            if score > max_score:
                max_score = score
        
        return max_score
    





# Leetcode optimal solution

class Solution(object):
    def maxScore(self, s):
        total_ones = s.count('1')
        left_zeros, right_ones = 0, total_ones
        max_score = 0

        for i in range(len(s)-1):
            left = s[:i]
            right= s[i:]

            if s[i] == '0':
                left_zeros += 1
            else:
                right_ones -= 1

            max_score = max(max_score, left_zeros+ right_ones)

        return max_score

            

      
        