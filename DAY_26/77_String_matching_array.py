'''Given an array of string words, return all strings in words that are a substring of another word. You can return the answer in any order.

 

Example 1:

Input: words = ["mass","as","hero","superhero"]
Output: ["as","hero"]
Explanation: "as" is substring of "mass" and "hero" is substring of "superhero".
["hero","as"] is also a valid answer.
Example 2:

Input: words = ["leetcode","et","code"]
Output: ["et","code"]
Explanation: "et", "code" are substring of "leetcode".
Example 3:

Input: words = ["blue","green","bu"]
Output: []
Explanation: No string of words is substring of another string.'''






# My logic simple and easy 

class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        result = []
        for i in range(len(words)):
            for j in range(len(words)):
                if i != j:
                    if words[i] in words[j]:
                        if words[i] not in result:
                            result.append(words[i])
        return result
    





# Leetcode best solution

class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        out = []
        for word in words:
            for w in words:
                if word == w:
                    continue
                if word in w:
                    out.append(word)
                    break
        return out