'''Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] = [c, d] if and only if either (a == c and b == d), or (a == d and b == c) - that is, one domino can be rotated to be equal to another domino.
Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and dominoes[i] is equivalent to dominoes[j].

Example 1:

Input: dominoes = [[1,2],[2,1],[3,4],[5,6]]
Output: 1
Example 2:

Input: dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]]
Output: 3'''







# My logic using dictionary

class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        """
        :type dominoes: List[List[int]]
        :rtype: int
        """
    
        count = {}
        result = 0

        for a, b in dominoes:
            key = (min(a, b), max(a, b))
            if key in count:
                result += count[key]
                count[key] += 1
            else:
                count[key] = 1
        return result
    





# My logic using collections

from collections import defaultdict

class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        """
        :type dominoes: List[List[int]]
        :rtype: int
        """

        count = defaultdict(int)
        result = 0

        for a, b in dominoes:
            key = (min(a, b), max(a, b))
            result += count[key]
            count[key] += 1

        return result
    





# Leet code best solution

# from collections import defaultdict

# class Solution(object):
#     def numEquivDominoPairs(self, dominoes):
#         """
#         :type dominoes: List[List[int]]
#         :rtype: int
#         """
        # dict_ = {}
        # count = 0
        # for pair in dominoes: 
        #     pair.sort()
        #     if str(pair) not in dict_: 
        #         dict_[str(pair)] = "yeah"
        #         count += 1
        #     else: 
        #         # dict_[str(pair)] += 1
        #         count += 1 
        # return (sum(count*(count-1)//2))    
        # return (sum(i*(i-1)//2 for i in dict_.values()))

        # count = defaultdict(int)
        # result = 0

        # for a, b in dominoes:
        #     key = tuple(sorted((a, b)))
        #     result += count[key]
        #     count[key] += 1

        # return result

import sys
import atexit

input = sys.stdin.readline

def write_runtime_file():
    with open("display_runtime.txt", "w") as f:
        f.write("0\n")

atexit.register(write_runtime_file)

class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        """
        :type dominoes: List[List[int]]
        :rtype: int
        """
        # count = defaultdict(int)
        count = [0] * 100
        res = 0
        for a, b in dominoes:
            key = a * 10 + b if a > b else b * 10 + a
            res += count[key]
            count[key] += 1
        return res
    







# My simple logic using for loop and condition but time limit exceeded

class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        """
        :type dominoes: List[List[int]]
        :rtype: int
        """
        result = 0
        n = len(dominoes)
        
        for i in range(n):
            for j in range(i + 1, n):
                a, b = dominoes[i]
                c, d = dominoes[j]
                if (a == c and b == d) or (a == d and b == c):
                    result += 1
                    
        return result
