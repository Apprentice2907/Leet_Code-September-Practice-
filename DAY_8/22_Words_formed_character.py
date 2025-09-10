'''You are given an array of strings words and a string chars.
A string is good if it can be formed by characters from chars (each character can only be used once for each word in words).
Return the sum of lengths of all good strings in words.

Example 1:

Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation: The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
Example 2:

Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Output: 10
Explanation: The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.'''







# My logic using loops and conditions

class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        result = 0
    
        for word in words:
            temp_chars = list(chars)  
            can_form = True
            
            for c in word:
                if c in temp_chars:
                    temp_chars.remove(c)  
                else:
                    can_form = False
                    break
                    
            if can_form:
                result += len(word)
                
        return result
    






# Leet code best solution

from collections import Counter

class Solution(object):
    def countCharacters(self, words, chars):
        res=0
        for c in words:
            for l in c:
                if c.count(l)>chars.count(l):
                    break
            else:
                res += len(c)
        return res