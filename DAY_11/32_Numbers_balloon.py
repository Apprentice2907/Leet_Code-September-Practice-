'''Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.

Example 1:

Input: text = "nlaebolko"
Output: 1
Example 2:

Input: text = "loonbalxballpoon"
Output: 2
Example 3:

Input: text = "leetcode"
Output: 0
 '''







# My logic 

class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        freq = {}
        for ch in text:
            freq[ch] = freq.get(ch, 0) + 1
        
        b = freq.get('b', 0) // 1
        a = freq.get('a', 0) // 1
        l = freq.get('l', 0) // 2
        o = freq.get('o', 0) // 2
        n = freq.get('n', 0) // 1
        
        return min(b, a, l, o, n)
    





# Leet code best solution

from collections import defaultdict

class Solution(object):
    def maxNumberOfBalloons(self, text):
        storage = defaultdict(int)
        
        # for letter in text:
        #     storage[letter] += 1
        
        b = text.count('b')//1
        a = text.count('a')//1
        l = text.count('l')//2
        o = text.count('o')//2
        n = text.count('n')//1
        
        ans = min(b,a,l,o,n)
        return ans
    
        #balloon
            