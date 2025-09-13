'''Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
Example 2:

Input: arr = [1,2]
Output: false
Example 3:

Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true'''









# My logic using brute force method

class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        freq = []
        for i in range(len(arr)):
            count = 0
            counted = False
            for k in range(i):
                if arr[i] == arr[k]:
                    counted = True
                    break
            if counted:
                continue
            for j in range(len(arr)):
                if arr[i] == arr[j]:
                    count += 1
            freq.append(count)

        for i in range(len(freq)):
            for j in range(i + 1, len(freq)):
                if freq[i] == freq[j]:
                    return False
        return True
    





# Leet code best solution

from collections import Counter
class Solution(object):
    def uniqueOccurrences(self, arr):
        count=Counter(arr)
        return len(set(count.values()))==len(count.values())
        