'''You are given an integer n.

We need to group the numbers from 1 to n according to the sum of its digits. For example, the numbers 14 and 5 belong to the same group, whereas 13 and 3 belong to different groups.

Return the number of groups that have the largest size, i.e. the maximum number of elements.

 

Example 1:

Input: n = 13
Output: 4
Explanation: There are 9 groups in total, they are grouped according sum of its digits of numbers from 1 to 13:
[1,10], [2,11], [3,12], [4,13], [5], [6], [7], [8], [9].
There are 4 groups with largest size.
Example 2:

Input: n = 2
Output: 2
Explanation: There are 2 groups [1], [2] of size 1.'''






# My logic and little bit chatGPT

class Solution(object):
    def countLargestGroup(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        groups = [0] * 100
        for num in range(1, n+1):
            s = 0
            for d in str(num):
                s += int(d)
            groups[s] += 1
        max_size = max(groups)
        count = 0
        for size in groups:
            if size == max_size:
                count += 1
        return count





# Leet code best solution

class Solution:
    def countLargestGroup(self, n):
        if n <= 0:
            return 0
        sd = [0] * (n + 1)         
        counts = {}
        for x in range(1, n + 1):
            sd[x] = sd[x // 10] + (x % 10)
            s = sd[x]
            counts[s] = counts.get(s, 0) + 1
        m = max(counts.values())
        return sum(v == m for v in counts.values())
