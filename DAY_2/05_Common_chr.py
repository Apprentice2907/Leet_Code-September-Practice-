'''Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.

Example 1:

Input: words = ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: words = ["cool","lock","cook"]
Output: ["c","o"]'''







# My logic using set of every element and then check if that exist then append it to the result list

class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        comchr = set(words[0])
        for word in words[1:]:
            comchr &= set(word)  

        result = []
        for char in comchr:
            minc = min(word.count(char) for word in words)
            result.extend([char] * minc)

        return result
    






 
# logic using iterative

class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        temp = list(words[0])
        for word in words[1:]:
            new_temp = []
            word_list = list(word)
            for char in temp:
                if char in word_list:
                    new_temp.append(char)
                    word_list.remove(char)
            temp = new_temp
        return temp










# Leet code best solution

class Solution(object):
    def commonChars(self, words):
        l=[]
        for c in set(words[0]):
            m=min(word.count(c) for word in words)
            l.extend([c]*m)
        return l