'''Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time, return that integer.

Example 1:

Input: arr = [1,2,2,6,6,6,6,7,10]
Output: 6
Example 2:

Input: arr = [1,1]
Output: 1
 '''







# My logic and also best approach leetcode best solution

class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        val = n * 0.25
        count = 1
        for i in range(1, n):
            if arr[i] == arr[i-1]:
                count += 1
                if count > val:
                    return arr[i]
            else:
                count = 1
        return arr[0]  